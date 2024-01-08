from uuid import UUID
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Reply
from django.shortcuts import get_object_or_404


class ToggleReplyDislikeView(APIView):
    def post(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                request.data["id"] = UUID(request.data["id"])
            except:
                pass

        reply = get_object_or_404(Reply, id=id)

        hasDisLiked = reply.dislikes.filter(
            id=request.user.profile.id).exists()

        hasLiked = reply.likes.filter(id=request.user.profile.id).exists()

        if hasDisLiked:
            reply.dislikes.remove(request.user.profile)
            reply.dislike_counts = reply.dislike_counts - 1
            reply.save()
        else:
            reply.dislikes.add(request.user.profile)
            reply.dislike_counts = reply.dislike_counts + 1
            reply.save()

        if hasLiked:
            reply.likes.remove(request.user.profile)
            reply.like_counts = reply.like_counts - 1
            reply.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
