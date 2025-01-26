from django.shortcuts import render, redirect

from areas.models import Area
from sports_spaces.models import SportsSpace
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def home_view(request):
    featured_areas = Area.objects.all()[:3]

    # si la busqueda se presenta se redirije a espacios con parametros de:
    if any(param in request.GET for param in ['deporte', 'ciudad', 'buscar']):
        base_url = reverse('areas_list_user_view')
        params = request.GET.urlencode()
        return redirect(f'{base_url}?{params}')

    return render(request, 'main/home.html', {
        'featured_areas': featured_areas,
        'sports': SportsSpace.SPORTS_TYPES,
    })
