from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['phone', 'note']  # user 與 event 從 view 填，不給用戶選
        labels = {
            'phone': '聯絡電話',
            'note': '備註',
        }