from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps

from billing.models import Bill
from .forms import ReservationForm
from django.http import JsonResponse
from decimal import Decimal
from datetime import datetime, date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

Reservation = apps.get_model('reservations', 'Reservation')

def is_staff_user(user):
    return user.is_staff


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, '', {'reservations': reservations})

@login_required
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    return render(request, '', {'reservation': reservation})

from datetime import datetime, timedelta

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user

            # Obtener horas de inicio y fin
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # Obtener el espacio y el área asociada
            space = form.cleaned_data['space']
            area = space.area

            # Validar que las horas estén dentro del horario permitido del área
            if start_time < area.opening_time or end_time > area.closing_time:
                return JsonResponse(
                    {
                        'success': False,
                        'message': f"El horario debe estar dentro del rango: {area.opening_time} - {area.closing_time}.",
                    },
                    status=400,
                )

            # Calcular la duración de la reserva en horas
            duration = (datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)).seconds / 3600
            hours = Decimal(duration)  # Convertir a Decimal para compatibilidad

            # Validar que las horas sean exactas
            if duration % 1 != 0:
                return JsonResponse({'success': False, 'message': 'Las horas deben ser exactas (por ejemplo, 13:00, 14:00).'}, status=400)

            # Calcular el precio total
            reservation.price = reservation.space.cost_per_hour * hours
            reservation.save()

            Bill.objects.create(
                reservation=reservation,
                user=request.user,
                status='Pendiente'
            )

            # Respuesta JSON para éxito
            return JsonResponse({'success': True, 'message': 'Espacio reservado con éxito.'})

        # Respuesta JSON para errores del formulario
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    # Respuesta en caso de método no permitido
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)


@login_required
@user_passes_test(is_staff_user)
def manage_reservations(request):
    reservations = Reservation.objects.all().order_by('-date', 'start_time')

    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        if reservation_id:
            try:
                reservation = Reservation.objects.get(id=reservation_id)
                reservation.delete()
                messages.success(request, "La reserva se eliminó correctamente.")
            except Reservation.DoesNotExist:
                messages.error(request, "La reserva no existe.")
        return redirect('manage_reservations')

    return render(request, 'reservations/owner_manage_reservations.html', {'reservations': reservations})