from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.publication_list, name='publication_list'),
    path('like/<int:pk>/', views.like_publication, name='like_publication'),
    path('comment/<int:publication_id>/', views.add_comment, name='add_comment'),
]