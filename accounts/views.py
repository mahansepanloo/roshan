from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token






class UserRegistersView(APIView):
	"""
	register user
	"""
	serializer_class = UserRegisterSerializer
	def post(self, request):
		ser_data = UserRegisterSerializer(data=request.data)
		if ser_data.is_valid():
			ser_data.create(ser_data.validated_data)
			return Response(ser_data.data, status=status.HTTP_201_CREATED)
		return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)





class LogoutView(APIView):
	"""
	logout user and remove token
	"""

	permission_classes = [IsAuthenticated]
	def post(self, request):
		user = request.user
		Token.objects.get(user=user).delete()
		return Response(status=status.HTTP_200_OK)