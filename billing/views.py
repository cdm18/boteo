from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.models import Bill
from reservations.models import Reservation
from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user)
def bill_list(request):
    selected_status = request.GET.get('status')

    bills = Bill.objects.filter(reservation__space__area__user = request.user).order_by('-created_at')

    # Aplicar filtro si se seleccionó un estado
    if selected_status:
        bills = bills.filter(status=selected_status)

    reservationCount = Reservation.objects.filter(status='Pendiente').count()

    context = {
        'bills': bills,
        'selected_status': selected_status,
        'reservationCount': reservationCount
    }

    return render(request, 'billing/bill_list.html', context)

@login_required
def update_bill_status(request, bill_id):
    # Obtiene la factura específica por su ID
    bill = get_object_or_404(Bill, id=bill_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
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
            reservation.save()
            bill.save()
            messages.success(request, f"El estado de la factura {bill.id} se actualizó a {bill.get_status_display()}.")
        else:
            messages.error(request, "Estado inválido seleccionado.")
        return redirect('bill_list')

    return render(request, 'billing/update_bill_status.html', {'bill': bill})