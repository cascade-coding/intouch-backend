from uuid import UUID
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Profile
from users.serializers import FindProfileSerializer
from django.shortcuts import get_object_or_404


class HandleFollowingView(APIView):
    def post(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                request.data["id"] = UUID(request.data["id"])
            except:
                pass

        serializer = FindProfileSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        profile = get_object_or_404(Profile, id=serializer.data.get("id"))

        if profile in request.user.profile.following.all():
            request.user.profile.following.remove(profile)
        else:
            request.user.profile.following.add(profile)

        return Response(status=status.HTTP_204_NO_CONTENT)
