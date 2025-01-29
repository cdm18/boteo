from django.urls import path
from .views import areas_list_view, area_detail, create_area, areas_list_user_view, area_detail_user_view

urlpatterns = [
    path('my_areas/', areas_list_view, name='my_areas'),
    path('my_areas/<int:pk>/', area_detail, name='area_detail'),
    path('create_area/', create_area, name='create_area'),
    path('', areas_list_user_view, name='areas_list_user_view'),
    path('<int:pk>/', area_detail_user_view, name='area_detail_user_view')
]