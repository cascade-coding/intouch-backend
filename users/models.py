from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.managers import UserManager
from django.core.mail import send_mail
import uuid
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from cloudinary.models import CloudinaryField


GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    following = models.ManyToManyField(
        'self', related_name='followers', symmetrical=False, blank=True
    )

    total_followers = models.IntegerField(default=0)

    total_following = models.IntegerField(default=0)

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

    def __str__(self):
        return self.user.username
