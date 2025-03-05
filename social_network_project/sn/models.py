from django.db import models
from users.models import User


class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    repost = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    hashtags = models.ManyToManyField('Hashtag', related_name='post', blank=True)

    def __str__(self):
        return f"Post by {self.author.username} - {self.created_at}"

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'
