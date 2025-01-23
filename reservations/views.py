from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.apps import apps
from sports_spaces.models import SportsSpace
from .forms import ReservationForm

Reservation = apps.get_model('reservations', 'Reservation')

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

@login_required
def create_reservation(request):
    spaces = SportsSpace.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.price = reservation.space.cost_per_hour
            reservation.save()
            return redirect('reservations:reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/create_reservation.html', {'form': form, 'spaces': spaces})