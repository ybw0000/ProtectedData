from django import forms
from .models import Contact, Invite


class ContactForm(forms.ModelForm):
    name = forms.TextInput
    email = forms.EmailInput
    phone = forms.TextInput
    message = forms.Textarea
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

class InviteForm(forms.ModelForm):
    email = forms.EmailInput
    class Meta:
        model = Invite
        fields = ['email']