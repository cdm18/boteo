from django.shortcuts import render, redirect
from sports_spaces.models import SportsSpace
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def home_view(request):
    # top 3 espacios por rating
    featured_spaces = SportsSpace.objects.all().order_by('-rating')[:3]

    # si la busqueda se presenta se redirije a espacios con parametros de:
    if any(param in request.GET for param in ['deporte', 'ciudad', 'buscar']):
        base_url = reverse('spaces_list')
        params = request.GET.urlencode()
        return redirect(f'{base_url}?{params}')

    return render(request, 'main/home.html', {
        'featured_spaces': featured_spaces,
        'sports': SportsSpace.SPORTS_TYPES,
    })

