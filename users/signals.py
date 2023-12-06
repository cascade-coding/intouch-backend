from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from users.models import User, Profile, Comment, Reply, Post


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if (created):
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.following.set([instance.profile.id])
        user_profile.save()


@receiver(m2m_changed, sender=Profile.following.through)
def update_connection_count(sender, instance, **kwargs):
    instance.total_followers = instance.following.count()
    instance.total_following = instance.followers.count()
    instance.save()


@receiver(post_save, sender=Comment)
def update_comment_count(sender, instance, created, **kwargs):
    if (created):
        instance.post.comment_counts = instance.post.comments.count()
        instance.post.save()


@receiver(post_save, sender=Reply)
def update_comment_reply_count(sender, instance, created, **kwargs):
    if (created):
        instance.comment.reply_counts = instance.comment.replies.count()
        instance.comment.save()