from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination
from rest_framework.views import APIView
from users.models import Profile, Post
from users.serializers import TrendingPostInfoSerializer
from django.shortcuts import get_object_or_404


class ProfilePostsView(APIView, CursorPagination):
    page_size = 5
    ordering = ['-created_at']

    def get(self, request, profile_id=None):
        user_profile = get_object_or_404(Profile, id=profile_id)

        posts = user_profile.posts.all()

        paginated_posts = self.paginate_queryset(
            posts, request=request
        )

        serializer = TrendingPostInfoSerializer(
            instance=paginated_posts, many=True, context={"request": request}
        )

        return self.get_paginated_response(
            serializer.data
        )


class DeletePostView(APIView):
    def post(self, request):
        post_id = request.data.get("postId", None)

        post = get_object_or_404(Post, id=post_id)

        user_profile = request.user.profile

        if (post.profile.id == user_profile.id):
            post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
