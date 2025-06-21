#專案urls.py

from django.contrib import admin
from django.urls import path , include
from django.views.generic.base import RedirectView 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/' , include('user.urls')),
    path('events/' , include('events.urls')),
    path('memberdashboard/' , include('memberdashboard.urls')),
    path('line_bot/' , include('line_bot.urls')),
    path('', RedirectView.as_view(url='/events/events_list/', permanent=False)),
    path('openai/', include('ai.urls')),
]

