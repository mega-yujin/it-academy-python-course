from rest_framework import serializers
from news.models import Article, ArticleImage, Category, FavoriteArticle

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')