# sports_spaces/views.py
from django.shortcuts import render, get_object_or_404
from .models import SportsSpace
from django.contrib.auth.decorators import login_required

@login_required
def spaces_list(request):
    # Obtén los valores enviados desde el formulario
    sport = request.GET.get('sport', '')  # Tipo de deporte
    city = request.GET.get('city', '')    # Ciudad
    name = request.GET.get('name', '')    # Nombre

    # Filtra los espacios deportivos basados en los valores
    spaces = SportsSpace.objects.all()

    if sport:
        spaces = spaces.filter(areas__sport_type=sport)
    if city:
        spaces = spaces.filter(city__icontains=city)
    if name:
        spaces = spaces.filter(name__icontains=name)

    # Asegúrate de no incluir duplicados al filtrar por áreas
    spaces = spaces.distinct()

    return render(request, 'sports_spaces/sports_space_list.html', {'spaces': spaces})


@login_required
def space_detail(request, pk):
    space = get_object_or_404(SportsSpace, pk=pk)
    return render(request, 'sports_spaces/space_detail.html', {'space': space})
