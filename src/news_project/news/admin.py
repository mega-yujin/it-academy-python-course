from django.contrib import admin
from . import models
from django.http import HttpRequest
from django.db.models import QuerySet

admin.site.site_title = 'Приложение для новостей'
admin.site.site_header = 'Приложение для новостей'
admin.site.index_title = 'Администрирование'

class CategoryInlineModel(admin.TabularInline):
    model = models.Article.categories.through
    extra = 2

@admin.register(models.Article)
class ArticleAdminView(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'favorites', )
    list_filter = ('author', 'favorites')
    actions = ('mark_as_favorite', 'unmark_as_favorite')
    inlines = [CategoryInlineModel]

    def mark_as_favorite(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(favorites=True)

    mark_as_favorite.short_description = 'Отметить как избранные'

    def unmark_as_favorite(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(favorites=False)

    unmark_as_favorite.short_description = 'Удалить из избранного'

    def clear_category(self, request: HttpRequest, queryset: QuerySet):
        for article in queryset:
            article.categories.clear()

    clear_category.short_description = 'Очистить категорию'