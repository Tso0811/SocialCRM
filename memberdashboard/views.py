from django.shortcuts import render
from events.models import Registration

def attended_events(request):
    registrations = Registration.objects.all()
    return render(request , 'attended_events.html' , {'registrations':registrations})
