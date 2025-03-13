from django.contrib import admin
from .models import Article, Category
from django.http import HttpRequest
from django.db.models import QuerySet

admin.site.site_title = 'News app'
admin.site.site_header = 'News app'
admin.site.index_title = 'Administration'


@admin.register(Article)
class ArticleAdminView(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'owner', 'is_published')
    list_filter = ('owner', 'is_published')
    actions = ('privatise', 'unprivatise')

    fieldsets = (
        (
            'Primary', {
                'fields': ('title', 'content', 'category'),
                'description': 'Primary information',
            }
        ),
        (
            'Secondary', {
                'fields': ('created_at', 'owner', 'is_published'),
                'classes': ('collapse', ),
                'description': 'Secondary information',
            }
        ),
    )

    def publish(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_published=True)

    def unpublish(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdminView(admin.ModelAdmin):
    list_display = ('name', )