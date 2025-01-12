from areas.models import Area
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AreaCreationForm

# Create your views here.
@login_required
def areas_list_view(request):
    areas = Area.objects.filter(user=request.user)
    return render(request, "areas/areas.html", {'areas': areas})

@login_required
def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    return render(request, 'areas/area_detail.html', {'area': area})


@login_required
def create_area(request):
    if request.method == 'POST':
        form = AreaCreationForm(request.POST, request.FILES)
        if form.is_valid():
            area = form.save(commit=False)
            area.user = request.user
            area.save()
            return redirect('my_areas')  # O donde quieras redirigir después de crear
    else:
        form = AreaCreationForm()

    return render(request, 'areas/create_area.html', {'form': form})