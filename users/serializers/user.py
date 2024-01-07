from rest_framework import serializers
from users.models import Profile, User
from djoser.serializers import UserSerializer as DjoserUserSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id", "profile_photo", "total_followers",
            "total_following", "total_posts"
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
