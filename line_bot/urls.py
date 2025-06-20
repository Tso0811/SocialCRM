#linebot urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'line_bot'

urlpatterns = [
    path('line_webhook/', views.line_webhook, name='line_webhook')
]

