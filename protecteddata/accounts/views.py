from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
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

def PassResetView(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = request.POST['email']
            finded_users = User.objects.filter(Q(email = data))
            if finded_users.exists():
                for user in finded_users:
                    subject = "Password reset"
                    email_template_name = 'registration/pass_reset_email.txt'
                    c = {
                        'email': user.email,
                        'domain': 'localhost',
                        'site_name': 'Protected Data',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'ProtectedData@gmail.com', [user.email], fail_silently = False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return render('password_reset_done.html')
    pass_reset_form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', context={'pass_reset_form': pass_reset_form})




