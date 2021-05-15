from django.urls import path
from . import views

urlpatterns = [
    path('', views.registr, name='registr'),
]