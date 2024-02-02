from django.urls import path
from .views import counter_view

app_name = 'stimulus-basic'

urlpatterns = [
    path('counter/', counter_view, name='counter'),
]