from django.urls import path
from .views import PermissionListCreateView

urlpatterns = [
    path('permissions', PermissionListCreateView.as_view()),
]