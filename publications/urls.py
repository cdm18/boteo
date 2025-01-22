from django.urls import path
from publications.views import *

app_name = 'publications'

urlpatterns = [
    path('', publication_list, name='publication_list'),
    path('like/<int:pk>/', like_publication, name='like_publication'),
    path('comment/<int:publication_id>/', add_comment, name='add_comment'),
]