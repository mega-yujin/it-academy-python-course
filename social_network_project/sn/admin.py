from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest
from django.db.models import QuerySet
from .models import Post, Comment, Hashtag
from users.models import User


@admin.register(User)
class UserAdminView(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_verified')
    list_filter = ('is_staff', 'is_superuser', 'is_verified')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'bio', 'avatar')}),
        ('Permissions',
         {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Post)
class PostAdminView(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at', 'is_private')
    list_filter = ('is_private', 'created_at', 'author')
    search_fields = ('content', 'author__username')
    actions = ('privatise', 'unprivatise')

    def privatise(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_private=True)

    def unprivatise(self, request: HttpRequest, queryset: QuerySet):
        queryset.update(is_private=False)


@admin.register(Comment)
class CommentAdminView(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username', 'post__content')


@admin.register(Hashtag)
class HashtagAdminView(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
