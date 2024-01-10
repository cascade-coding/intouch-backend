from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers.profile import EditProfileSerializer
from rest_framework import status


class DeleteAccountView(APIView):
    def post(self, request):
        password = request.data.get("password", None)

        user = request.user

        is_valid = user.check_password(password)

        if (not is_valid):
            return Response({"message": "invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
