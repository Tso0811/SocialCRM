from django.shortcuts import render , redirect
from .models import Events , Registration
from .forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

def events_list(request): #顯示所有活動
    events = Events.objects.all()
    return render(request , 'events_list.html' , {'events':events})

def event_detail(request , id):
    event = get_object_or_404(Events , id = id)
    return render(request , 'event_detail.html' , {'event':event} )

@login_required
def event_edit(request , id):
    event = get_object_or_404(Events , id = id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        content = request.POST.get('content')

        event.title = title
        event.date = date
        event.content = content

        event.save()
        return redirect('events:events_list')
    return render(request , 'event_edit.html' , {'event':event})

@login_required
def event_register(request, id):
    event = get_object_or_404(Events, id = id)
    
    if Registration.objects.filter(user = request.user , event = event):
        return render (request ,'event_registered.html' , {'event':event})
        
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit = False)
            registration.user = request.user
            registration.event = event
            registration.save()

            send_mail(
            subject='活動報名成功',
            message='您好，恭喜你活動報名成功！',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,            #預設為False  信件發送錯誤會拋出錯誤訊息 在正式環境中要設為True
            )                                        
            return redirect("events:event_detail", id = event.id)
    else:
        form = RegistrationForm()
    return render(request, "event_register.html", {"form": form, "event": event})

@login_required
def event_attendees(request , id):
    event = get_object_or_404(Events , id = id)
    registrations = Registration.objects.filter(event = event)
    return render (request , 'event_attendees.html' ,{'event':event , 'registrations':registrations})