from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Detail


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = (
            'id',
            'name',
            'created_date'
        )
        read_only_fields = (
            'id',
        )


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    is_staff = serializers.BooleanField(required=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
