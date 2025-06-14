#events urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events_list/' , views.events_list , name = 'events_list' ),
    path('event_detail/<int:id>/' , views.event_detail , name = 'event_detail'),
    path('event_edit/<int:id>/' , views.event_edit , name = 'event_edit' ),
    path('event_register/<int:id>/', views.event_register, name='event_register'),
    path('event_registered<int:id>' , views.event_register , name = 'event_registered' ),
]

