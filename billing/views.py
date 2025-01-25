from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.forms import BillForm
from billing.models import Bill
from reservations.models import Reservation


@login_required
def bill_list(request):
    if request.user.user_type == 1:
        bills = Bill.objects.all().order_by('-created_at')
    else:
        bills = Bill.objects.all().order_by('-created_at')

    return render(request, 'billing/bill_list.html', {'bills': bills})

@login_required
def update_bill_status(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Bill.BILL_STATUS_CHOICES):
            bill.status = new_status
            bill.save()
            messages.success(request, f"El estado de la factura {bill.id} se actualizó a {bill.get_status_display()}.")
        else:
            messages.error(request, "Estado inválido seleccionado.")
        return redirect('bill_list')

    return render(request, 'billing/update_bill_status.html', {'bill': bill})

@login_required
def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST, user=request.user)
        if form.is_valid():
            bill = form.save(commit=False)

            if not bill.reservation:
                dummy_reservation = Reservation.objects.create(
                    user=request.user,
                    space=bill.space,
                )
                bill.reservation = dummy_reservation

            bill.save()
            return redirect('billing:bill_list')
    else:
        form = BillForm(user=request.user)

    return render(request, 'billing/create_bill.html', {'form': form})
