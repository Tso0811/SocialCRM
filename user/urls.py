#user urls.py

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/' , views.login_view , name = 'login'),
    path('register' , views.register , name = 'register'),
    path('logout/' , views.logout_view , name = 'logout')
]
