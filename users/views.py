from rest_framework.pagination import CursorPagination
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from users.models import Profile, User, Post
from users.serializers import SuggestionsProfileSerializer, UserProfileSerializer, PostSerializer, PostInfoSerializer, TrendingPostInfoSerializer


class GetSuggestions(APIView):
    def get(self, request):
        try:
            user_profile = Profile.objects.get(
                user_id=request.user.id
            )

            serializer = UserProfileSerializer(instance=user_profile)

            following = serializer.data["following"]

            following_ids = list(map(str, following))

            following_ids.append(request.user.profile.id)

            records = Profile.objects.exclude(
                id__in=following_ids
            ).exclude(user__is_active=False)[:6]

            serializer = SuggestionsProfileSerializer(
                instance=records, many=True
            )

            return Response({"suggestions": serializer.data})
        except:
            return Response({"message": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddNewPostView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get("text", None)
        images = request.data.get("images", None)

        if not text and not images:
            return Response(
                {"message": "Invalid fields."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(
            data={"text": text},
            context={"request": request}
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        post = Post.objects.get(id=serializer.data["id"])

        info_serializer = PostInfoSerializer(instance=post)

        return Response(
            info_serializer.data,
            status=status.HTTP_201_CREATED
        )


class GetHomePosts(APIView, CursorPagination):
    page_size = 50
    ordering = '-trend_score'

    def get(self, request):
        user_profile = Profile.objects.get(user_id=request.user.id)

        date_range = timezone.now() - timedelta(days=5)

        # Get the posts of the users they are following
        following = user_profile.following.all()

        following_posts = Post.objects.filter(
            profile__in=following,
            created_at__gte=date_range
        )

        trending_posts = following_posts.annotate(
            trend_score=F('like_counts') + F('comment_counts') * 2
        ).order_by('-trend_score')

        paginated_posts = self.paginate_queryset(
            trending_posts, request=request)

        serializer = TrendingPostInfoSerializer(
            instance=paginated_posts, many=True
        )

        return self.get_paginated_response(
            {"posts": serializer.data}
        )
