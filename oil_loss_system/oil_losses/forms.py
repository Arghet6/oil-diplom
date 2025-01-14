from django import forms
from .models import OilLossRecord

class OilLossRecordForm(forms.ModelForm):
    class Meta:
        model = OilLossRecord
        fields = ['date', 'location', 'oil_type', 'estimated_loss', 'actual_loss', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']