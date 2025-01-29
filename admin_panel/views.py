from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from reservations.models import Reservation


def is_staff_user(user):
    return user.is_staff

@user_passes_test(is_staff_user)
def admin_panel_view(request):
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    return render(request, 'admin_panel/admin_panel.html', {'reservationCount': reservationCount})