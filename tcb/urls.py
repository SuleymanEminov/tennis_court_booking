from django.urls import path
from . import views

app_name = 'tcb'

urlpatterns = [
    path('', views.index, name='index'),
]