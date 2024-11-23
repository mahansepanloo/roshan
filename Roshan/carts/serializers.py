from rest_framework import serializers



class AddCartSerializer(serializers.Serializer):
    num = serializers.IntegerField(default=1, min_value=1)