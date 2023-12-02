from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import Profile, User
from users.serializers import SuggestionsProfileSerializer, UserProfileSerializer


class GetSuggestions(APIView):
    def get(self, request):
        try:
            user_profile = Profile.objects.get(
                user_id=request.user.id
            )

            serializer = UserProfileSerializer(instance=user_profile)

            following = serializer.data["following"]

            following_ids = list(map(str, following))

            following_ids.append(request.user.profile.id)

            records = Profile.objects.exclude(
                id__in=following_ids
            ).exclude(user__is_active=False)[:6]

            serializer = SuggestionsProfileSerializer(
                instance=records, many=True)

            return Response({"suggestions": serializer.data})
        except:
            return Response({"message": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
