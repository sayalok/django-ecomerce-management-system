from django.urls import path
from .views import UserRoleListCreateView

urlpatterns = [
    path('user_roles', UserRoleListCreateView.as_view()),
]