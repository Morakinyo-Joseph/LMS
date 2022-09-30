from django import forms
from .models import User


class AccountCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )
        labels = {
            "email": "Email Address",
            "password2": "Confirm Password"
        }        
