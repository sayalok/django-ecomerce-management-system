from django.urls import path
from .views import getallusers, register, login, AuthenticatedUser, logout

urlpatterns = [
    path('', getallusers),
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('user_details', AuthenticatedUser.as_view())
]
