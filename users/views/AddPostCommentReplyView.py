from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Reply, Comment
from users.serializers import AddPostCommentReplySerializer, PostCommentReplySerializer
from django.shortcuts import get_object_or_404


class AddPostCommentReplyView(APIView):
    def post(self, request):
        comment_id = request.data.get("comment_id", None)

        if comment_id is None:
            return Response(
                {"message": "comment Id is required"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        comment = get_object_or_404(Comment, id=comment_id)
        request.data["comment"] = comment.id
        request.data["profile"] = request.user.profile.id

        serializer = AddPostCommentReplySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()

            reply_obj = get_object_or_404(Reply, id=serializer.data["id"])

            new_reply = PostCommentReplySerializer(
                instance=reply_obj, context={"request": request}
            )
            return Response(
                new_reply.data,
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
