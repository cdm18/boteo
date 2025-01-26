from django.urls import path
from . import views


urlpatterns = [
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/<int:bill_id>/edit/', views.update_bill_status, name='update_bill_status'),
]
