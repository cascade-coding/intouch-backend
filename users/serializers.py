from rest_framework import serializers
from users.models import Profile, User, Comment, Reply, Post, PostImage


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "profile_photo"]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


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


"""
 post related serializers
"""


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'text')


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'replies')


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'image')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'like_counts', 'text')

    def create(self, validated_data):
        images_data = self.context.get('request').data.getlist(
            'images'
        )

        user = self.context.get('request').user

        profile = Profile.objects.get(user=user)

        new_post = Post.objects.create(
            **validated_data, profile=profile
        )

        image_added = 0

        for image_data in images_data:
            image_added = image_added + 1

            if image_added >= 10:
                break

            PostImage.objects.create(
                post=new_post, image=image_data
            )

        return new_post


class PostInfoSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'like_counts', 'comments', 'text', 'post_images')


class ProfileInfoSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "profile_photo", "user"]


class TrendingPostInfoSerializer(serializers.ModelSerializer):
    profile = ProfileInfoSerializer(read_only=True)
    post_images = PostImageSerializer(many=True)
    user_liked = serializers.SerializerMethodField()
    user_disliked = serializers.SerializerMethodField()

    def get_user_liked(self, post):
        request = self.context.get('request', None)
        return post.likes.filter(id=request.user.profile.id).exists()

    def get_user_disliked(self, post):
        request = self.context.get('request', None)
        return post.dislikes.filter(id=request.user.profile.id).exists()

    class Meta:
        model = Post
        fields = (
            'id', 'profile', 'user_liked', 'user_disliked', 'like_counts', 'dislike_counts',
            'comment_counts', 'text', 'post_images'
        )


class FindProfileSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class FindPostSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class PostCommentSerializer(serializers.ModelSerializer):
    profile = ProfileInfoSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "profile",
            "text",
            "like_counts",
            "dislike_counts",
            "reply_counts",
            "created_at"
        ]
