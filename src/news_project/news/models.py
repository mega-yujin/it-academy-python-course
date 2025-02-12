from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.CharField(max_length=500, verbose_name='Описание категории')


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(verbose_name='Creation date', default=timezone.now)
    is_published = models.BooleanField(verbose_name='Published?', default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.SET_NULL, null=True)
    favorite = models.ForeignKey(
        User, related_name='favorite_articles', blank=True,  null=True, on_delete=models.SET_NULL
    )
    id = models.UUIDField(primary_key=True, default=uuid4)


class ArticleFile(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='files', verbose_name='Article'
    )
    file = models.ImageField(upload_to='news_files/', verbose_name='File')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Upload date')

    class Meta:
        verbose_name = 'Article file'
        verbose_name_plural = 'Article files'

    def __str__(self):
        return f'Article files {self.article.title}'
