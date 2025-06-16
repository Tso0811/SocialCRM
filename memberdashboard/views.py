from django.shortcuts import render , redirect
from events.models import Registration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

@login_required
def attended_events(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request , 'attended_events.html' , {'registrations':registrations})

@login_required
def cancel_registration(request , id ):
    registration = get_object_or_404(Registration , event__id = id , user = request.user)
    if request.method == 'POST' and not request.user.is_company:
        registration.delete()
        return redirect('memberdashboard:attended_events')
    return render(request , 'cancel_registration.html' , {'registration':registration})
