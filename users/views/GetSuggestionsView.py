from rest_framework.pagination import CursorPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Profile
from users.serializers import SuggestionsProfileSerializer


class GetSuggestionsView(APIView, CursorPagination):
    page_size = 15
    ordering = '-total_followers'

    def get(self, request):
        try:
            top = request.GET.get("top", None)

            following = request.user.profile.following.all()

            top_profiles = Profile.objects.exclude(
                id__in=following
            ).exclude(user__is_active=False).order_by('-total_followers')

            if top:
                top_profiles = top_profiles[:5]

                serializer = SuggestionsProfileSerializer(
                    instance=top_profiles, many=True, context={"request": request}
                )

                return Response({"suggestions": serializer.data})

            paginated_profiles = self.paginate_queryset(
                top_profiles, request=request
            )

            serializer = SuggestionsProfileSerializer(
                instance=paginated_profiles, many=True, context={"request": request}
            )

            return self.get_paginated_response(
                serializer.data
            )

        except:
            return Response({"message": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
