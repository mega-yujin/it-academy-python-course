from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тег')
    description = models.TextField(null=True, blank=True, verbose_name='Описание тега')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_favorite = models.BooleanField(default=False, verbose_name='Избранное')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', related_name='notes')
    tags = models.ManyToManyField(Tag, related_name='notes', verbose_name='Теги', blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        permissions = [
            ('can_mark_as_fav', 'Can mark notes as favorite'),
        ]

    def __str__(self):
        return self.title


class NoteFile(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='files', verbose_name='Заметка')
    file = models.FileField(upload_to='notes_files/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    class Meta:
        verbose_name = 'Файл заметки'
        verbose_name_plural = 'Файлы заметки'

    def __str__(self):
        return f'Файлы доя заметки {self.note.title}'
