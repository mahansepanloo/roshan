from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class UserRegisterSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True, required=True)
	class Meta:
		model = User
		fields = ('username', 'password', 'password2')
		read_only_fields = ('id',)

	def create(self, validated_data):
		del validated_data['password2']
		return User.objects.create_user(**validated_data)

	def validated_email(self, value):
		if User.objects.filter(email=value).exists():
			raise serializers.ValidationError('This email already exists')
		return  value

	def validate_username(self, value):
		if value == 'admin':
			raise serializers.ValidationError('username cant be `admin`')
		return value

	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('passwords must match')
		return data


