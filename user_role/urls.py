from django.urls import path
from .views import UserRoleListCreateView, UserRoleRetriveUpdateDelete

urlpatterns = [
    path('user_roles', UserRoleListCreateView.as_view()),
    path('user_role/<int:pk>', UserRoleRetriveUpdateDelete.as_view()),
]