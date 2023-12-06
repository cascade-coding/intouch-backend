# Generated by Django 4.2.7 on 2023-12-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_rename_likes_count_post_like_counts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_counts',
            new_name='reply_counts',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='reply_counts',
        ),
        migrations.AddField(
            model_name='post',
            name='comment_counts',
            field=models.IntegerField(default=0),
        ),
    ]
