from rest_framework.pagination import CursorPagination
from django.db.models import F
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from users.models import Profile, Post
from users.serializers import TrendingPostInfoSerializer


class GetHomePostsView(APIView, CursorPagination):
    page_size = 10
    ordering = '-trend_score'

    def get(self, request):
        user_profile = Profile.objects.get(user_id=request.user.id)

        date_range = timezone.now() - timedelta(days=5)

        # Get the posts of the users they are following
        following = user_profile.following.all()

        following_posts = Post.objects.filter(
            profile__in=following,
            # created_at__gte=date_range
        )

        # if no posts found in the range of last five days
        if not following_posts:
            following_posts = Post.objects.filter(
                profile__in=following
            )

        # if there is no posts at all
        if not following_posts:
            top_profiles = Profile.objects.exclude(
                id__in=following
            ).exclude(user__is_active=False).order_by('-total_followers')[:6]

            following_posts = Post.objects.filter(
                profile__in=top_profiles,
                created_at__gte=date_range
            )

        trending_posts = following_posts.annotate(
            trend_score=F('like_counts') + F('comment_counts') * 2
        ).order_by('-trend_score')

        paginated_posts = self.paginate_queryset(
            trending_posts, request=request
        )

        serializer = TrendingPostInfoSerializer(
            instance=paginated_posts, many=True, context={"request": request}
        )

        return self.get_paginated_response(
            serializer.data
        )
