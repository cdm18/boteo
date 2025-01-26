from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_reservation, name='create_reservation'),
    path('manage/', views.manage_reservations, name='manage_reservations'),
]
