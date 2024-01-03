from django.db import models
import uuid
from users.models import Profile, Post


class Comment(models.Model):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE,
        related_name='comments', null=True, blank=True
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    likes = models.ManyToManyField(
        to=Profile, related_name='comment_likes', blank=True
    )

    dislikes = models.ManyToManyField(
        to=Profile, related_name='comment_dislikes', blank=True
    )

    like_counts = models.IntegerField(default=0)

    dislike_counts = models.IntegerField(default=0)

    text = models.TextField()

    reply_counts = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    comment = models.ForeignKey(
        to=Comment, on_delete=models.CASCADE, related_name='replies'
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    likes = models.ManyToManyField(
        to=Profile, related_name='reply_likes', blank=True
    )

    dislikes = models.ManyToManyField(
        to=Profile, related_name='reply_dislikes', blank=True
    )

    like_counts = models.IntegerField(default=0)

    dislike_counts = models.IntegerField(default=0)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
