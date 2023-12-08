from rest_framework import serializers
from users.models import Profile, User, Comment, Reply, Post, PostImage


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
        fields = ["id", "profile_photo",
                  "total_followers", "total_following", "user"]


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


class TrendingPostInfoSerializer(serializers.ModelSerializer):
    post_images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'like_counts', 'dislike_counts',
            'comment_counts', 'text', 'post_images'
        )
