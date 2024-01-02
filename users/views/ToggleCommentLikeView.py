from uuid import UUID
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Comment
from django.shortcuts import get_object_or_404


class ToggleCommentLikeView(APIView):
    def post(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                request.data["id"] = UUID(request.data["id"])
            except:
                pass

        comment = get_object_or_404(Comment, id=id)

        hasLiked = comment.likes.filter(id=request.user.profile.id).exists()

        hasDisLiked = comment.dislikes.filter(
            id=request.user.profile.id).exists()

        if hasLiked:
            comment.likes.remove(request.user.profile)
            comment.like_counts = comment.like_counts - 1
            comment.save()
        else:
            comment.likes.add(request.user.profile)
            comment.like_counts = comment.like_counts + 1
            comment.save()

        if hasDisLiked:
            comment.dislikes.remove(request.user.profile)
            comment.dislike_counts = comment.dislike_counts - 1
            comment.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
