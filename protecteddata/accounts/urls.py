from django.urls import path

from .views import SignUpView, LoginView, PassResetView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView, name='signup'),
    path('login/', LoginView, name='login'),
    path('password_reset/', PassResetView, name = 'passresetview'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name = 'password_reset_confirm')
]