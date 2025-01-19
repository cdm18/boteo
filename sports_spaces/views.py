from django.shortcuts import render, get_object_or_404
from .models import SportsSpace
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
@login_required
def spaces_list(request):
    sport = request.GET.get('deporte', '')
    city = request.GET.get('ciudad', '')
    search = request.GET.get('buscar', '')

    spaces = SportsSpace.objects.all()

    if sport:
        spaces = spaces.filter(sport_type=sport)
    if city:
        spaces = spaces.filter(location__icontains=city)
    if search:
        spaces = spaces.filter(name__icontains=search)

    # Define imágenes por defecto según el tipo de deporte
    for space in spaces:
        if not space.image:
            if space.sport_type == 'Fútbol':
                space.default_image = 'img/futbol-default.jpg'
            elif space.sport_type == 'Ecuavoley':
                space.default_image = 'img/ecuavoley-default.jpg'
            elif space.sport_type == 'Piscina':
                space.default_image = 'img/piscina-default.jpg'
            else:
                space.default_image = 'img/default.jpg'

    paginator = Paginator(spaces, 6)
    page = request.GET.get('page')
    spaces = paginator.get_page(page)

    # parametros de busqueda
    context = {
        'spaces': spaces,
        'sports': SportsSpace.SPORTS_TYPES,
        'current_sport': sport,
        'current_city': city,
        'current_search': search,
    }
    return render(request, 'sports_spaces/sports_space_list.html', context)
@login_required
def space_detail(request, pk):
    space = get_object_or_404(SportsSpace, pk=pk)
    return render(request, 'sports_spaces/space_detail.html', {'space': space})
