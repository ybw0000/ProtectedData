from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import SignUpForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def SignUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password = raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', context={'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Login or password is not correct')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', context={'form': form})
