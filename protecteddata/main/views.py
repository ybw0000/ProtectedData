from django.shortcuts import render, redirect
from .forms import ContactForm, InviteForm, NewslettersForm
from .models import Contact, Invite
from django.http import HttpResponseRedirect

# def index(request):
#     return render(request, 'main/index.html')

def index(request):
    error = False
    contact_form = ContactForm()
    invite_form = InviteForm()
    newsletter_form = NewslettersForm()
    if request.method == 'POST':
        if 'Contact' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('index')
        if 'EmailInvite' in request.POST:
            invite_form = InviteForm(request.POST)
            if invite_form.is_valid():
                invite_form.save()
                return redirect('index')
        if 'Newsletters' in request.POST:
            newsletter_form = NewslettersForm(request.POST)
            if newsletter_form.is_valid():
                newsletter_form.save()
                return redirect('index')
    else:
        contact_form = ContactForm()
        invite_form = InviteForm()
        newsletter_form = NewslettersForm()
    data = {
        'contact_form': contact_form,
        'error': error,
        'invite_form': invite_form,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'main/index.html', data)