from django.urls import path
from .views import spaces_list, space_detail

urlpatterns = [
    path('', spaces_list, name='spaces_list'),
    path('<int:pk>/', space_detail, name='space_detail'),
]
