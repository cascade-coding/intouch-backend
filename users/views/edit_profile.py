from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers.profile import EditProfileSerializer


class EditProfileView(APIView):
    def get(self, request):
        profile = request.user.profile
        serializer = EditProfileSerializer(instance=profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.profile
        serializer = EditProfileSerializer(
            instance=profile, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
