from rest_framework import viewsets
from news.models import Category, Article, ArticleImage, FavoriteArticle
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer