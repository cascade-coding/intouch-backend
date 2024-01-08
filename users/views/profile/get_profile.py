from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class GetProfileView(APIView):
    def get(self, request, username=""):
        profile = get_object_or_404(
            User, username__iexact=username
        )

        serializer = UserSerializer(
            instance=profile,
        )

        return Response(serializer.data)
