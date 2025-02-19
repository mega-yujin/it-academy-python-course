from rest_framework import viewsets, permissions
from news.models import Category, Article, ArticleImage, FavoriteArticle
from .serializers import CategorySerializer, ArticleSerializer, ArticleCreationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreationSerializer
        return ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def favorites(self, request):
        favorite_articles = self.Article.objects.filter(favoritearticle__user=request.user)
        serializer = self.get_serializer(favorite_articles, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_fav(self, request):
        article = self.get_object()
        user = request.user
        favorite_article, created = FavoriteArticle.objects.get_or_create(user=user, article=article)
        if not created:
            favorite_article.delete()
            return Response()
        article.save()
        return Response()
