from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime

from areas.models import Area
from billing.models import Bill
from reservations.models import Reservation
from sports_spaces.models import SportsSpace
from django.db.models import Sum

def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def admin_panel_view(request):
    today = datetime.today()
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    totalReservations = Reservation.objects.all().count()
    todayReservations = Reservation.objects.filter(date=today).count()
    totalAreas = Area.objects.filter(user=request.user).count()
    totalSpaces = SportsSpace.objects.filter(area__user=request.user).count()

    totalIncome = Bill.objects.filter(status='Pagado').aggregate(
        total=Sum('reservation__price')
    )['total'] or 0

    payedBills = Bill.objects.filter(status='Pagado').count()

    return render(request, 'admin_panel/admin_panel.html',
                  {'reservationCount': reservationCount,
                   'totalReservations': totalReservations,
                   'todayReservations': todayReservations,
                   'totalAreas': totalAreas,
                   'totalSpaces': totalSpaces,
                   'totalIncome': totalIncome,
                   'payedBills': payedBills})
