from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from areas.models import Area
from sports_spaces.models import SportsSpace
from .forms import AreaCreationForm


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
@login_required
def areas_list_view(request):
    areas = Area.objects.filter(user=request.user)
    return render(request, "areas/areas.html", {'areas': areas})


@user_passes_test(is_staff_user)
@login_required
def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    sports_spaces = SportsSpace.objects.filter(area=area)
    pk = area.pk
    if request.method == "POST" and request.POST.get('action') == 'delete':
        area.delete()
        messages.success(request, 'Espacio deportivo eliminado exitosamente.')
        return redirect('my_areas')
    if request.method == "POST":
        form = AreaCreationForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            area.save()
            messages.success(request, 'Espacio deportivo actualizado exitosamente.')
            return redirect('area_detail', pk=pk)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    if request.method == "GET":
        form = AreaCreationForm(instance=area)
        return render(request, 'areas/area_detail.html', {'area': area, 'form': form, 'sport_spaces': sports_spaces})


@user_passes_test(is_staff_user)
@login_required
def create_area(request):
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

    return render(request, 'areas/create_area.html', {'form': form})
