from rest_framework import serializers
from rest_framework.response import Response

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Generic serializer for users"""

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


class UserRegisterSerializer(serializers.ModelSerializer):

    """Serializer for user registration view"""

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password == password2:
            user = CustomUser(**validated_data)
            user.set_password(password)
            # New users should not be active
            user.is_active = False
            # TODO: Send registration confirmation
            user.save()
            return user
        else:
            raise serializers.ValidationError({"detail": "Passwords do not match."})
