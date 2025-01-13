from django.shortcuts import render, get_object_or_404, redirect
from .models import Pago
def gestion_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'facturacion/gestion_factura.html', {'pagos': pagos})

def marcar_pagado(request, id):
    if request.method == 'POST':
        pago = get_object_or_404(Pago, id=id)
        if pago.estado != 'Pagado':
            pago.estado = 'Pagado'
            pago.save()
        return redirect('gestion_pagos')
    return redirect('gestion_pagos')

def editar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        estado = request.POST.get('estado')
        pago.estado = estado
        pago.save()
        return redirect('gestion_pagos')
    return render(request, 'facturacion/editar_factura.html', {'pago': pago})

def eliminar_pago(request, pk):
    pago = get_object_or_404(Pago, pk=pk)
    if request.method == 'POST':
        pago.delete()
        return redirect('gestion_pagos')


def crear_factura(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        correo = request.POST.get('correo')
        monto = request.POST.get('monto')
        estado = request.POST.get('estado')
        Pago.objects.create(cliente=cliente, correo=correo, monto=monto, estado=estado)
        return redirect('gestion_pagos')
    return render(request, 'facturacion/crear_factura.html')