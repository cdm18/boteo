from django.urls import path
from .views import areas_list_view, area_detail, create_area

urlpatterns = [
    path('', areas_list_view, name='my_areas'),
    path('<int:pk>/', area_detail, name='area_detail'),
    path('create_area/', create_area, name='create_area'),
]
