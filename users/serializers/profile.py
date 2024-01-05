from rest_framework import serializers
from users.models import Profile
from users.serializers import UserInfoSerializer


class SuggestionsProfileSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    is_following = serializers.SerializerMethodField()

    def get_is_following(self, profile):
        request = self.context.get('request', None)
        return profile.followers.filter(id=request.user.profile.id).exists()

    class Meta:
        model = Profile
        fields = [
            "id", "profile_photo",
            "total_followers", "total_following", "user", "is_following"
        ]


class ProfileInfoSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "profile_photo", "user"]


class FindProfileSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class EditProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "id", "profile_photo", "name",
            "bio", "gender", "date_of_birth"
        ]
