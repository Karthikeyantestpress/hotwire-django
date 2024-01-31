from django.urls import path
from .views import create_view, list_view

app_name = 'turbo-drive'

urlpatterns = [
    path('list/', list_view, name='task-list'),               
    path('create/', create_view, name='task-create'),
]