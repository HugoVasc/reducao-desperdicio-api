from rest_framework import serializers
from accounts import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = ""
        if 'username' in validated_data:
            username = validated_data['username']
        else:
            username = validated_data['email']
        user = models.Usuario(
            username=username,
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user