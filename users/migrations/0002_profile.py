# Generated by Django 4.2.7 on 2023-12-08 18:40

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_followers', models.IntegerField(default=0)),
                ('total_following', models.IntegerField(default=0)),
                ('profile_photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='profile_photo')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('bio', models.TextField(blank=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='users.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]