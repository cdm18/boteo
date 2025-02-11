from django.db import IntegrityError
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

from .models import Reservation


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
            try:
                reservation = form.save(commit=False)
                reservation.user = request.user

                # Calcular duración y precio
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                duration = (datetime.combine(date.min, end_time) - datetime.combine(date.min,
                                                                                    start_time)).seconds / 3600
                hours = Decimal(str(duration))

                reservation.price = reservation.space.cost_per_hour * hours
                reservation.save()

                # Crear factura asociada
                Bill.objects.create(
                    reservation=reservation,
                    user=request.user,
                    status='Pendiente'
                )

                return JsonResponse({
                    'success': True,
                    'message': 'Espacio reservado con éxito.'
                })
            except IntegrityError:
                return JsonResponse({
                    'success': False,
                    'message': 'Ya existe una reserva para este espacio en el horario seleccionado.'
                }, status=400)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': f'Error al crear la reserva: {str(e)}'
                }, status=400)

        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)

    return JsonResponse({
        'success': False,
        'message': 'Método no permitido.'
    }, status=405)


@login_required
@user_passes_test(is_staff_user)
def manage_reservations(request):
    reservations =  Reservation.objects.filter(space__area__user = request.user).order_by('-date', 'start_time')


    if request.method == 'POST':
        reservation_id = request.POST.get('reservation_id')
        action = request.POST.get('action')

        if reservation_id:
            try:
                reservation = Reservation.objects.get(id=reservation_id)

                if action == 'accept' and reservation.status == 'Pendiente':
                    reservation.status = 'Confirmado'
                    reservation.save()
                    messages.success(request, f"La reserva {reservation.id} ha sido aceptada.")

                elif action == 'mark_paid' and reservation.status == 'Confirmado':
                    bill = Bill.objects.filter(reservation=reservation).first()
                    if bill:
                        bill.status = 'Pagado'
                        bill.save()
                        messages.success(request, f"La reserva {reservation.id} ha sido marcada como pagada.")

                elif action == 'cancel' and reservation.status in ['Pendiente', 'Confirmado']:
                    reservation.status = 'Cancelada'
                    reservation.save()

                    bill = Bill.objects.filter(reservation=reservation).first()
                    if bill:
                        bill.status = 'Cancelado'
                        bill.save()

                    messages.success(request, f"La reserva {reservation.id} ha sido cancelada.")

                else:
                    messages.error(request, "Acción no permitida o estado inválido para la reserva.")

            except Reservation.DoesNotExist:
                messages.error(request, "La reserva no existe.")
            except Exception as e:
                messages.error(request, f"Error al procesar la acción: {str(e)}")

        return redirect('manage_reservations')

    return render(request, 'reservations/owner_manage_reservations.html', {'reservations': reservations})