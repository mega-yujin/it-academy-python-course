from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect, render
from .models import Article, Category
from .serializers import ArticleSerializer, ArticleCreateSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('article-list')  # Redirect to the article list page
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')


class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    renderer_classes = [renderers.TemplateHTMLRenderer]
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in (
                'create', 'create_article', 'update_article', 'partial_update', 'update'
        ):
            return ArticleCreateSerializer
        return ArticleSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['categories'] = Category.objects.all()
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response({
            'articles': queryset,
        }, template_name='index.html')

    def retrieve(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = self.get_serializer(article)
        return Response({'article': serializer.data}, template_name='news/article_detail.html')

    @action(
        detail=True, methods=['get', 'post'], url_path='delete', url_name='delete',
        permission_classes=[permissions.IsAuthenticated]
    )
    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        if self.request.method == 'POST':
            article.delete()
            return redirect('article-list')
        return Response({'article': article}, template_name='news/delete_article.html')

    @action(
        detail=True, methods=['post'], url_path='toggle_fav', url_name='toggle_fav',
        permission_classes=[permissions.IsAuthenticated],
    )
    def toggle_fav(self, request, pk=None):
        article = self.get_object()
        if request.user in article.favorites.all():
            article.favorites.remove(request.user)
        else:
            article.favorites.add(request.user)
        article.save()
        return redirect('article-list')

    @action(
        detail=False, methods=['get'], url_path='create', url_name='create',
        permission_classes=[permissions.IsAuthenticated],
    )
    def create_form(self, request):
        serializer = self.get_serializer()
        return Response(
            {
                'serializer': serializer,
                'categories': Category.objects.all()
             },
            template_name='news/add_article.html'
        )

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data.setlist('categories', request.POST.getlist('categories'))

        if 'images' in mutable_data and not request.FILES.getlist('images'):
            mutable_data.pop('images')

        serializer = self.get_serializer(data=mutable_data)

        if not serializer.is_valid():
            return Response({
                'serializer': serializer,
                'categories': Category.objects.all()
            }, template_name='news/add_article.html')

        article = serializer.save(owner=request.user)

        return redirect('article-detail', pk=article.pk)

    def update(self, request, *args, **kwargs):
        article = self.get_object()

        if request.method == 'GET':
            serializer = self.get_serializer(article)
            return Response({
                'article': article,
                'serializer': serializer,
                'categories': Category.objects.all()
            }, template_name='news/update_article.html')

        mutable_data = request.data.copy()
        mutable_data.setlist('categories', request.POST.getlist('categories'))

        serializer = self.get_serializer(
            article,
            data=mutable_data,
            partial=True
        )

        if not serializer.is_valid():
            return Response({
                'article': article,
                'serializer': serializer,
                'categories': Category.objects.all()
            }, template_name='news/news/update_article.html')

        serializer.save()
        return redirect('article-detail', pk=article.pk)
