from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Post, Comment
from users.serializers import AddPostCommentSerializer,  PostCommentSerializer
from django.shortcuts import get_object_or_404


class AddPostCommentView(APIView):
    def post(self, request):
        post_id = request.data.get("post_id", None)

        if post_id is None:
            return Response(
                {"message": "post Id is required"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        post = get_object_or_404(Post, id=post_id)
        request.data["post"] = post.id
        request.data["profile"] = request.user.profile.id

        serializer = AddPostCommentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()

            comment_obj = get_object_or_404(Comment, id=serializer.data["id"])

            new_comment = PostCommentSerializer(instance=comment_obj)

            return Response(
                new_comment.data,
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
