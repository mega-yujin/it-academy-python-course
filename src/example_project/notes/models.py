from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тег')
    description = models.TextField(null=True, blank=True, verbose_name='Описание тега')

    def __str__(self):
        return self.name


class Note(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid4, help_text='Уникальный идентификатор заметки')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    file = models.FileField(upload_to='notes_files/', null=True, blank=True, verbose_name='Файл')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранное')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='notes')
    tags = models.ManyToManyField(Tag, related_name='notes', verbose_name='Теги', blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
