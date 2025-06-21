from django.urls import path
from .views import recommend_events

urlpatterns = [
    path('recommend/', recommend_events, name='recommend_events'),
]