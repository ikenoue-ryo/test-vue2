from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import Post, Category
from .serializers import CategorySerializer, PostSerializer

class CategoryListApiView(generics.ListAPIView):
    """カテゴリモデルの取得（一覧）APIクラス"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer