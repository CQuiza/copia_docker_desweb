from rest_framework import serializers # para crear las clases
from django.contrib.auth.models import User # para manejar usuarios con django
from .models import Owners, Deptos, Mpios # importar el modelo de la app1


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owners
        fields = '__all__'

class DeptosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deptos
        fields = '__all__'

class MpiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpios
        fields = '__all__'