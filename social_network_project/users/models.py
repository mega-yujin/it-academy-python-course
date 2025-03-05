from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    is_verified = models.BooleanField(default=False)
    friends = models.ManyToManyField('self', related_name='friends', blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='friendreq_sent',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name='friendreq_received',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_user', 'to_user')