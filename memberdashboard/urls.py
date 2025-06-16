#member_dashboard urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'memberdashboard'

urlpatterns = [
    path('attended_events/' , views.attended_events , name = 'attended_events'),
    path('cancel_registration/<int:id>' , views.cancel_registration , name = 'cancel_registration'), 
]

