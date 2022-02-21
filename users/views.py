from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView

from .authentication import generate_access_token, JWTAuthentication
from .models import User
from .serializers import UserSerializers


@api_view(['POST'])
def register(request):
    data = request.data

    if data['password'] != data['password_confirmation']:
        raise exceptions.APIException('password do not match')

    serializer = UserSerializers(data=data)
    if not serializer.is_valid(raise_exception=False):
        return Response({'Status': 'Failed', 'message': serializer.errors})
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')

    response = Response()

    token = generate_access_token(user)

    response.set_cookie(key="token", value=token, httponly=True)
    response.data = {
        'token': token
    }

    return response


@api_view(['GET'])
def getallusers(request):
    serializer = UserSerializers(User.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie(key="token")
    response.data = {
        'message': 'Success'
    }

    return response


class AuthenticatedUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializers(request.user)

        return Response({
            'data': serializer.data
        })
