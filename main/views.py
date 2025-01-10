from django.shortcuts import render
from sports_spaces.models import SportsSpace
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    featured_spaces = SportsSpace.objects.all()[:3]
    return render(request, 'home/home.html', {'featured_spaces': featured_spaces})
