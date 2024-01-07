from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from users.models import User

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]


class Profile(models.Model):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    following = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False, blank=True
    )

    total_followers = models.IntegerField(default=0)

    total_following = models.IntegerField(default=0)

    total_posts = models.IntegerField(default=0)

    profile_photo = CloudinaryField(
        'profile_photo', resource_type='image', blank=True
    )

    name = models.CharField(max_length=150, blank=True)

    bio = models.TextField(blank=True)

    date_of_birth = models.DateField(
        auto_now=False, auto_now_add=False,
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=30, choices=GENDER_CHOICES, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
