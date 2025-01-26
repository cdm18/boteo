from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.models import Bill
from reservations.models import Reservation


@login_required
def bill_list(request):
    bills = Bill.objects.all().order_by('-created_at')
    return render(request, 'billing/bill_list.html', {'bills': bills})

@login_required
def update_bill_status(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Bill.BILL_STATUS_CHOICES):
            bill.status = new_status
            reservation = bill.reservation
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
