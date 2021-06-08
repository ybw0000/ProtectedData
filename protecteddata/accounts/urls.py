from django.urls import path

from .views import SignUpView, LoginView, PassResetView


urlpatterns = [
    path('signup/', SignUpView, name='signup'),
    path('login/', LoginView, name='login'),
    path('password_reset/', PassResetView, name = 'passresetview'),
]