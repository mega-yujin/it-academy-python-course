from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.CharField(max_length=500, verbose_name='Описание категории')


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)
    is_published = models.BooleanField(verbose_name='Опубликована?', default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.SET_NULL, null=True)
    favorites = models.ManyToManyField(User, related_name='favorite_articles', blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4)
