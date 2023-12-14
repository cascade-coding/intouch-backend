from uuid import UUID
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Post
from users.serializers import FindPostSerializer
from django.shortcuts import get_object_or_404


class TogglePostLikeView(APIView):
    def post(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                request.data["id"] = UUID(request.data["id"])
            except:
                pass

        serializer = FindPostSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        post = get_object_or_404(Post, id=serializer.data.get("id"))

        if request.user.profile in post.likes.all():
            post.likes.remove(request.user.profile)
            post.like_counts = post.like_counts - 1
            post.save()
        else:
            post.likes.add(request.user.profile)
            post.like_counts = post.like_counts + 1
            post.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
