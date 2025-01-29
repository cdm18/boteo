from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.models import Bill
from reservations.models import Reservation


@login_required
def bill_list(request):
    # Obtiene todas las facturas ordenadas por fecha de creación descendente
    reservationCount = Reservation.objects.filter(status='Pendiente').count()
    bills = Bill.objects.all().order_by('-created_at')
    return render(request, 'billing/bill_list.html', {'bills': bills, 'reservationCount': reservationCount})

@login_required
def update_bill_status(request, bill_id):
    # Obtiene la factura específica por su ID
    bill = get_object_or_404(Bill, id=bill_id)

    if request.method == 'POST':
        # Obtiene el nuevo estado enviado en el formulario
        new_status = request.POST.get('status')
        # Verifica si el nuevo estado es válido
        if new_status in dict(Bill.BILL_STATUS_CHOICES):
            # Actualiza el estado de la factura
            bill.status = new_status
            # Obtiene la reserva asociada a la factura
            reservation = bill.reservation
            # Actualiza el estado de la reserva según el nuevo estado de la factura
            if new_status == Bill.BILL_STATUS_CHOICES[1][0]:
                reservation.status = Reservation.STATUS_CHOICES[1][0]
            elif new_status == Bill.BILL_STATUS_CHOICES[2][0]:
                reservation.status = Reservation.STATUS_CHOICES[2][0]
            else:
                reservation.status = Reservation.STATUS_CHOICES[2][0]
            # Guarda los cambios en la reserva y la factura
            reservation.save()
            bill.save()
            # Muestra un mensaje de éxito
            messages.success(request, f"El estado de la factura {bill.id} se actualizó a {bill.get_status_display()}.")
        else:
            # Muestra un mensaje de error si el estado es inválido
            messages.error(request, "Estado inválido seleccionado.")
        # Redirige a la lista de facturas
        return redirect('bill_list')

    # Renderiza el formulario de actualización de estado de factura
    return render(request, 'billing/update_bill_status.html', {'bill': bill})
