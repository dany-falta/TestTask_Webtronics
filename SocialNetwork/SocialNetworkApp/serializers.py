from http import HTTPStatus
import requests
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'author')


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_email(self, value):
        response = requests.get(settings.EMAIL_VALIDATOR_URL, params={
            'api_key': settings.EMAIL_VALIDATOR_KEY,
            'email': value
        })
 
        if response.status_code == HTTPStatus.OK and response.json()['data']['result'] == 'undeliverable':
            raise serializers.ValidationError('Undeliverable email')
        if response.status_code == HTTPStatus.OK and response.json()['data']['status'] == 'invalid':
            raise serializers.ValidationError('Invalid email')

        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user