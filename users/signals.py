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




@receiver(m2m_changed, sender=Post.likes.through)
@receiver(m2m_changed, sender=Post.dislikes.through)
def prevent_both(sender, instance, action, reverse, model, pk_set, **kwargs):
    print(pk_set, 'xx')
    print(instance, 'iii')
    if action == 'pre_add':
        if reverse:
            # User is trying to add a like/dislike to a post
            # Check if there are already dislikes and remove them
            if instance.dislikes.filter(pk__in=pk_set).exists():
                instance.dislikes.clear()
        else:
            # User is trying to add a post to likes/dislikes
            # Check if there are already likes and remove them
            if instance.likes.filter(pk__in=pk_set).exists():
                instance.likes.clear()