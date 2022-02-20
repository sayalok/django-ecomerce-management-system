from django.urls import path
from .views import getallusers, register, login

urlpatterns = [
    path('', getallusers),
    path('register', register),
    path('login', login)
]
