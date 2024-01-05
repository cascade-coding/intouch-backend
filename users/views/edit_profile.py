from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers.profile import EditProfileSerializer


class EditProfileView(APIView):
    def get(self, request):
        profile = request.user.profile
        serializer = EditProfileSerializer(instance=profile)
        return Response(serializer.data)
