from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User


class ActivateUsersView(APIView):
    def get(self, request):
        users = User.objects.filter(is_active=False)

        for user in users:
            user.is_active = True
            user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
