from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length= 100, verbose_name='Название категории')
    description = models.CharField(max_length=500, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
     title = models.CharField(max_length=100, verbose_name='Заголовок')
     content = models.TextField(verbose_name='Содержание')
     created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
     is_published = models.BooleanField(default=False, verbose_name='Опубликована?')
     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
     categories = models.ManyToManyField(Category, related_name='articles')
     favorites = models.BooleanField(default=False, verbose_name='Избранное')

     class Meta:
         ordering = ['-created_at']
         verbose_name = 'Статья'
         verbose_name_plural = 'Статьи'

     def __str__(self):
         return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='article_images/%Y/%m/%d/',
        verbose_name='Изображение',
        height_field='height',
        width_field='width'
    )
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.image:
            img = Image.open(self.image)

            if img.height > 1000 or img.width > 1000:
                output_size = (1000, 1000)
                img.thumbnail(output_size)

                img.save(self.image.path, quality=85, optimize=True)

            super().save(*args, **kwargs)