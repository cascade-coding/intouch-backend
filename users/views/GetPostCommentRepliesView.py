from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Reply
from users.serializers import PostCommentReplySerializer
from rest_framework.pagination import CursorPagination
from django.db.models import F


class GetPostCommentRepliesView(APIView, CursorPagination):
    page_size = 10
    ordering = "-trend_score"

    def post(self, request):
        id = request.data.get("id", None)

        if id is None:
            return Response(
                {"message": "comment Id is required"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        try:
            replies = Reply.objects.filter(comment_id=id).annotate(
                trend_score=F('like_counts') + F('dislike_counts') * 2
            ).order_by('-trend_score')

            paginated_replies = self.paginate_queryset(
                replies, request=request
            )

            serializer = PostCommentReplySerializer(
                instance=paginated_replies, many=True
            )
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return self.get_paginated_response(
            serializer.data
        )
