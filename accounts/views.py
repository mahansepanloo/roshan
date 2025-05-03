from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.core.cache import cache
from rest_framework.authtoken.models import Token
from random import randint
from .sms import send_otp_code


class UserRegistersView(APIView):
    """
    register user
    """

    serializer_class = UserRegisterSerializer

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        code = randint(100, 999)
        print(code)
        if ser_data.is_valid():
            info = {
                "username": ser_data.validated_data["username"],
                "password": ser_data.validated_data["password"],
                "otp": code,
            }

            phone_number = ser_data.validated_data["phone_number"]
            cache.set(phone_number, info, timeout=120)
            request.session["phone_number"] = phone_number
            # send_otp_code(phone_number,code)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class OtpCodeView(APIView):
    """
    check otp code and create_user
    """

    serializer_class = OtpSerializers

    def post(self, request):
        otp = OtpSerializers(data=request.data)
        if otp.is_valid():
            otp_code = cache.get(request.session["phone_number"])
            if not otp_code:
                return Response("not found code", status=status.HTTP_400_BAD_REQUEST)
            if otp_code["otp"] == otp.validated_data["code"]:
                User.objects.create_user(
                    username=otp_code["username"], password=otp_code["password"]
                )
                cache.delete(request.session["phone_number"])
                return Response("create user", status=status.HTTP_200_OK)
            return Response("not found code", status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    logout user and remove token
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.get(user=user).delete()
        return Response(status=status.HTTP_200_OK)
