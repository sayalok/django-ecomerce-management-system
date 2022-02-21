from rest_framework import serializers

from .models import UserRole
from permissions.serializers import PermissionsSerializer


class UserRolesSerializer(serializers.ModelSerializer):
    permissions = PermissionsSerializer(many=True)

    class Meta:
        model = UserRole
        fields = '__all__'
