from django.shortcuts import get_object_or_404
from rest_framework import generics, status, mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.authentication import JWTAuthentication
from .models import UserRole
from .serializers import UserRolesSerializer


class UserRoleListCreateView(generics.ListCreateAPIView):
    serializer_class = UserRolesSerializer

    def list(self, request):
        serializer = UserRolesSerializer(UserRole.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = UserRolesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class UserRoleRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin):
    serializer_class = UserRolesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserRole.objects.filter(pk=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            queryset = UserRole.objects.get(pk=self.kwargs['pk'])
            serializer = UserRolesSerializer(queryset)
            return Response({
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            raise exceptions.ValidationError('Not Found')

    def update(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            queryset = UserRole.objects.get(pk=self.kwargs['pk'])
            serializer = UserRolesSerializer(instance=queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'data': serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        else:
            raise exceptions.ValidationError('Not Found')

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response({
                'message': 'Success'
            }, status=status.HTTP_204_NO_CONTENT)
        else:
            raise exceptions.ValidationError('Not Found')
