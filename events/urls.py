#events urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events_list/' , views.events_list , name = 'events_list' ),
    path('event_detail/<int:id>' , views.event_detail , name = 'event_detail'),
]
