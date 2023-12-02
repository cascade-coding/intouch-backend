from rest_framework import serializers
from users.models import Profile, User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class SuggestionsProfileSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        model = Profile
        fields = ["id", "profile_photo", "user"]


class UUIDSerializer(serializers.Serializer):
    pass
    # class Meta:
    #     model = Profile
    #     fields = "__all__"
