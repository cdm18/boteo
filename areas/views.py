from areas.models import Area, AreaService, AdditionalService
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from reservations.models import Reservation
from sports_spaces.models import SportsSpace
from .forms import AreaCreationForm
from django.contrib import messages


# Create your views here.

def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user)
def areas_list_view(request):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    areas = Area.objects.filter(user=request.user)
    return render(request, "areas/areas.html", {'areas': areas, 'reservationCount': reservationCount})


@login_required
@user_passes_test(is_staff_user)
def area_detail(request, pk):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    area = get_object_or_404(Area, pk=pk)
    sports_spaces = SportsSpace.objects.filter(area=area)
    additional_services = AreaService.objects.filter(area=area).select_related('service')

    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'delete':
            area.delete()
            messages.success(request, 'Área deportiva eliminada exitosamente.')
            return redirect('my_areas')

        elif action == 'delete_service':
            try:
                service = AreaService.objects.get(
                    id=request.POST.get('service_id'),
                    area=area
                )
                service.delete()
                messages.success(request, 'Servicio eliminado exitosamente.')
                return redirect('area_detail', pk=pk)
            except AreaService.DoesNotExist:
                messages.error(request, 'Servicio no encontrado.')

        elif action == 'create_service':
            service = AdditionalService.objects.create(
                creator=request.user,
                name=request.POST.get('service_name')
            )
            AreaService.objects.create(
                area=area,
                service=service,
                is_available=True
            )
            messages.success(request, 'Servicio adicional creado exitosamente.')
            return redirect('area_detail', pk=pk)

        elif action == 'update_services':
            # Update service availability status
            for service in additional_services:
                status_field = f'service_{service.id}_status'
                is_available = status_field in request.POST
                if service.is_available != is_available:
                    service.is_available = is_available
                    service.save()
            messages.success(request, 'Servicios actualizados exitosamente.')
            return redirect('area_detail', pk=pk)

        else:
            # Handle area update
            form = AreaCreationForm(request.POST, request.FILES, instance=area)
            if form.is_valid():
                area = form.save()
                messages.success(request, 'Área deportiva actualizado exitosamente.')
                return redirect('area_detail', pk=pk)
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = AreaCreationForm(instance=area)

    return render(request, 'areas/area_detail.html', {
        'area': area,
        'form': form,
        'sport_spaces': sports_spaces,
        'additional_services': additional_services,
        'reservationCount': reservationCount
    })


@login_required
@user_passes_test(is_staff_user)
def create_area(request):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    if request.method == 'POST':
        form = AreaCreationForm(request.POST, request.FILES)
        if form.is_valid():
            area = form.save(commit=False)
            area.user = request.user
            area.save()
            messages.success(request, 'Espacio deportivo guardado exitosamente.')
            return redirect('my_areas')  # O donde quieras redirigir después de crear
    else:
        form = AreaCreationForm()

    return render(request, 'areas/create_area.html', {'form': form, 'reservationCount': reservationCount})


@login_required
def areas_list_user_view(request):
    areas = Area.objects.all()
    # Filtra según los parámetros GET (deporte, ciudad y búsqueda)
    deporte = request.GET.get('deporte', '')
    ciudad = request.GET.get('ciudad', '')
    buscar = request.GET.get('buscar', '')

    if deporte:
        areas = areas.filter(css__sport_type=deporte)

    if ciudad:
        areas = areas.filter(city__icontains=ciudad)

    if buscar:
        areas = areas.filter(name__icontains=buscar)

    # No duplicados
    areas = areas.distinct()


    # Pasa las áreas filtradas al contexto
    return render(request, "areas/areas_general_user.html", {'areas': areas,
                                                             'sports': SportsSpace.SPORTS_TYPES},
)


@login_required
def area_detail_user_view(request, pk):
    area = get_object_or_404(Area, pk=pk)
    additional_services = AreaService.objects.filter(area=area).select_related('service')
    sports_spaces = SportsSpace.objects.filter(area=area)
    return render(request, "areas/area_general_user_detail.html",
                  {'area': area, 'sport_spaces': sports_spaces, 'additional_services': additional_services})
