from django import forms
from .models import Registr

class RegistrForm(forms.ModelForm):
    class Meta:
        model = Registr
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "password1": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "password2": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
            }),
        }