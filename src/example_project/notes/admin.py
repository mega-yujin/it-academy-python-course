from django.contrib import admin
from .models import Note, Tag
from django.http import HttpRequest
from django.db.models import QuerySet

admin.site.site_title = 'Приложение для заметок'
admin.site.site_header = 'Приложение для заметок'
admin.site.index_title = 'Администрирование'


class TagsInlineModel(admin.TabularInline):
    model = Note.tags.through
    extra = 2
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'


@admin.register(Note)
class NotesAdminView(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'is_favorite')
    list_filter = ('owner', 'is_favorite')
    actions = ('mark_as_favorite', 'unmark_as_favorite')

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content'),
            'description': 'Основная информация'
        }
         ),
        ('Дополнительно', {
            'fields': ('owner', 'created_at', 'is_favorite', 'tags'),
            'classes': ('collapse',),
            'description': 'Дополнительная информация',
        }
         ),
    )
    inlines = (TagsInlineModel,)

    def mark_as_favorite(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_favorite=True)

    def unmark_as_favorite(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_favorite=False)
