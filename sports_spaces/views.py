# sports_spaces/views.py
from django.shortcuts import render, get_object_or_404, redirect

from areas.models import Area
from reservations.models import Reservation
from sports_spaces.models import SportsSpace
from django.contrib.auth.decorators import login_required, user_passes_test
from sports_spaces.forms import SportsSpaceForm
from django.contrib import messages



def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff_user)
def sport_space_detail_view(request, pk):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    sport_space = SportsSpace.objects.get(pk=pk)
    area = SportsSpace.objects.get(pk=pk).area
    form = SportsSpaceForm(request.POST, instance=sport_space)
    area_link = 'my_areas/' + str(area.pk)
    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'delete':
            sport_space.delete()
            messages.success(request, 'Espacio deportivo eliminado exitosamente.')
            return redirect('area_detail', area.pk)

        else:
            if form.is_valid():
                sport_space = form.save()
                messages.success(request, 'Espacio deportivo actualizado exitosamente.')
                return redirect('sport_space_detail', pk=pk)
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = SportsSpaceForm(instance=sport_space)

    return render(request, 'sports_spaces/sport_space_detail.html',
                  {'form': form,
                   "sport_space": sport_space,
                   "area": area,
                   "area_link": area_link,
                   'reservationCount': reservationCount})

@login_required
@user_passes_test(is_staff_user)
def create_space_view(request, pk):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    area = Area.objects.get(pk=pk)
    if request.method == 'POST':
        form = SportsSpaceForm(request.POST)
        if form.is_valid():
            sport_space = form.save(commit=False)
            sport_space.area = area
            sport_space.save()
            messages.success(request, 'Espacio deportivo guardado exitosamente.')
            return redirect('area_detail', pk)  # O donde quieras redirigir después de crear
    else:
        form = SportsSpaceForm()

    return render(request, 'sports_spaces/create_sport_space.html', {'form': form, 'area': area,'reservationCount': reservationCount})
