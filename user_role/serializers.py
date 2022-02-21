from rest_framework import serializers

from permissions.models import Permissions
from .models import UserRole
from permissions.serializers import PermissionsSerializer


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionsSerializer(value).data

    def to_internal_value(self, data):
        return data


class UserRolesSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = UserRole
        fields = '__all__'

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance
