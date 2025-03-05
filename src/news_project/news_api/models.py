from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.CharField(max_length=500, verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(verbose_name='Creation date', default=timezone.now)
    is_published = models.BooleanField(verbose_name='Published?', default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    categories = models.ManyToManyField(Category, related_name='articles', blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_articles', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4)


class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='images', verbose_name='Article'
    )
    images = models.ImageField(upload_to='news_images/', verbose_name='Images')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Upload date')

    class Meta:
        verbose_name = 'Article image'
        verbose_name_plural = 'Article images'

    def __str__(self):
        return f'Article image {self.article.title}'
