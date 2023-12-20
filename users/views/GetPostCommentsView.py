from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Comment
from users.serializers import PostCommentSerializer
from rest_framework.pagination import CursorPagination
from django.db.models import F


class GetPostCommentsView(APIView, CursorPagination):
    page_size = 10
    ordering = "-trend_score"

    def post(self, request):
        id = request.data.get("id", None)

        if id is None:
            return Response(
                {"message": "post Id is required"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        try:
            comments = Comment.objects.filter(post_id=id).annotate(
                trend_score=F('like_counts') + F('reply_counts') * 2
            ).order_by('-trend_score')

            paginated_comments = self.paginate_queryset(
                comments, request=request
            )

            serializer = PostCommentSerializer(
                instance=paginated_comments, many=True
            )
        except:
            return Response(
                {"message": "something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return self.get_paginated_response(
            serializer.data
        )
