from django.shortcuts import render
import jwt
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer

# Create your views here.
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class EmailConfirmAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        try:
            user = User.objects.get(id=decoded.get("user_id"))
        except User.DoesNotExist:
            return Response(data={"status": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        user.is_confirmed = True
        user.save()

        return Response(data={"status": "Confirmed!"}, status=status.HTTP_200_OK)


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)