from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
from .models import Permissions
from .serializers import PermissionsSerializer


class PermissionListView(generics.ListAPIView):
    serializer_class = PermissionsSerializer

    def get(self,request):
        serializer = PermissionsSerializer(Permissions.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })
