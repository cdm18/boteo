# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin_panel/', views.admin_panel_view, name='admin_panel'),
]