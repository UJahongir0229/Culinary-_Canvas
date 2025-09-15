from django.urls import path

from .views import (
    UserRegisterAPIView,
    EmailConfirmAPIView,
    UserLoginAPIView,
    )

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name="register"),
    path('register/confirm/<str:token>/', EmailConfirmAPIView.as_view(), name="register-confirm"),

    path('login/', UserLoginAPIView.as_view(), name="login"),
]