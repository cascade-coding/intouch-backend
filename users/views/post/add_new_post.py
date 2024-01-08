from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Post
from users.serializers import PostSerializer, TrendingPostInfoSerializer


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

        info_serializer = TrendingPostInfoSerializer(
            instance=post, context={"request": request}
        )

        return Response(
            info_serializer.data,
            status=status.HTTP_201_CREATED
        )
