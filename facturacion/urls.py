from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_pagos, name='gestion_pagos'),
    path('crear_factura/', views.crear_factura, name='crear_factura'),
    path('eliminar_pago/<int:id>/', views.eliminar_pago, name='eliminar_pago'),
    path('marcar_pagado/<int:id>/', views.marcar_pagado, name='marcar_pagado'),
]
