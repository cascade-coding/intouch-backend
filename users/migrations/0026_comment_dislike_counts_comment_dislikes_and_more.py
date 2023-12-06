# Generated by Django 4.2.7 on 2023-12-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_rename_comment_counts_comment_reply_counts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislike_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to='users.profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='like_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to='users.profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='dislike_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to='users.profile'),
        ),
        migrations.AddField(
            model_name='reply',
            name='dislike_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reply',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='reply_dislikes', to='users.profile'),
        ),
        migrations.AddField(
            model_name='reply',
            name='like_counts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reply',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='reply_likes', to='users.profile'),
        ),
    ]
