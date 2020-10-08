from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        filelds = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'