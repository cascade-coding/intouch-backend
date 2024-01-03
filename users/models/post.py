from django.db import models
import uuid
from users.models import Profile
from cloudinary.models import CloudinaryField


class Post(models.Model):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    profile = models.ForeignKey(
        to=Profile, related_name='posts', on_delete=models.CASCADE
    )

    text = models.TextField(blank=True, null=True, default=None)

    likes = models.ManyToManyField(
        to=Profile, related_name='likes', blank=True
    )

    dislikes = models.ManyToManyField(
        to=Profile, related_name='dislikes', blank=True
    )

    like_counts = models.IntegerField(default=0)

    dislike_counts = models.IntegerField(default=0)

    comment_counts = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def like_post(self, user_profile):
        if user_profile in self.dislikes.all():
            self.dislikes.remove(user_profile)
        self.likes.add(user_profile)

    def dislike_post(self, user_profile):
        if user_profile in self.likes.all():
            self.likes.remove(user_profile)
        self.dislikes.add(user_profile)


class PostImage(models.Model):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    post = models.ForeignKey(
        to=Post,
        related_name='post_images',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    image = CloudinaryField('image', resource_type='image')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
