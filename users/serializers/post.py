from rest_framework import serializers
from users.models import Post, PostImage, Profile
from users.serializers import CommentSerializer, ProfileInfoSerializer


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
            'comment_counts', 'text', 'post_images', 'created_at'
        )


class FindPostSerializer(serializers.Serializer):
    id = serializers.UUIDField()
