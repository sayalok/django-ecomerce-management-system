from django.urls import path
from .views import PermissionListView

urlpatterns = [
    path('permissions', PermissionListView.as_view()),
]