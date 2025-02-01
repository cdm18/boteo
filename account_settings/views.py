from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from account_settings.forms import UserProfileForm
from account_settings.models import UserProfile
from billing.models import Bill
from reservations.models import Reservation

# Vista para mostrar el perfil del usuario
@login_required
def profile_view(request):
    try:
        # Obtener el perfil del usuario actual
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Si no existe, se crea un perfil por defecto
        profile = UserProfile.objects.create(user=request.user)

    # Obtener todas las reservas del usuario
    payedReservations = Bill.objects.filter(user=request.user).filter(status='Pagado')
    total_reservations = len(payedReservations)
    bills = Bill.objects.filter(user=request.user)

    total_hours = 0
    for bill in payedReservations:
        # Calcular la duración de cada reserva
        start = datetime.combine(datetime.today(), bill.reservation.start_time)
        end = datetime.combine(datetime.today(), bill.reservation.end_time)
        delta = end - start
        total_hours += delta.total_seconds() / 3600

    total_hours = int(total_hours)

    context = {
        'profile': profile,
        'bills': bills,
        'total_hours': total_hours,
        'total_reservations': total_reservations,
    }
    return render(request, 'account_settings/profile.html', context)

# Vista para editar el perfil del usuario
@login_required
def edit_profile(request):
    # try:
        # Obtener el perfil del usuario actual
    profile = request.user.userprofile
    # except UserProfile.DoesNotExist:
    #     # Si no existe, se crea un perfil por defecto
    #     profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account_settings:profile')
    else:
        # Cargar el formulario con los datos actuales
        form = UserProfileForm(instance=profile)

    return render(request, 'account_settings/edit_profile.html', {'form': form})
