from rest_framework import generics
from rest_framework.response import Response

from .models import UserRole
from .serializers import UserRolesSerializer


class UserRoleListCreateView(generics.ListAPIView):
    serializer_class = UserRolesSerializer

    def list(self, request):
        serializer = UserRolesSerializer(UserRole.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })
