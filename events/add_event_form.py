from django import forms
from .models import Events

class Add_event_form (forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title' , 'date' , 'content']