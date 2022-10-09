from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Follower(models.Model):
    """
    Follower model related to owner and followed.
    The 'owner' is a user that is following a user.
    'followed' is the user that is followed by the 'owner'
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed'
        )
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    """
    Preventing user's to dubplicate following.
    """
    ordering = ['-created_at']
    unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
