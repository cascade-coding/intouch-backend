from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import Profile
from users.serializers import SuggestionsProfileSerializer


class SearchProfileView(APIView):
    def get(self, request, search=""):
        profile = Profile.objects.filter(user__username__iexact=search)

        serializer = SuggestionsProfileSerializer(
            instance=profile,
            many=True,
            context={"request": request}
        )

        return Response({"profiles": serializer.data})
