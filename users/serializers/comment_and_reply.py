from rest_framework import serializers
from users.models import Comment, Reply
from users.serializers import ProfileInfoSerializer

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'text')


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'replies')


class PostCommentSerializer(serializers.ModelSerializer):
    profile = ProfileInfoSerializer(read_only=True)
    user_liked = serializers.SerializerMethodField()
    user_disliked = serializers.SerializerMethodField()

    def get_user_liked(self, comment):
        request = self.context.get('request', None)
        return comment.likes.filter(id=request.user.profile.id).exists()

    def get_user_disliked(self, comment):
        request = self.context.get('request', None)
        return comment.dislikes.filter(id=request.user.profile.id).exists()

    class Meta:
        model = Comment
        fields = [
            "id",
            "profile",
            "text",
            "user_liked",
            "user_disliked",
            "like_counts",
            "dislike_counts",
            "reply_counts",
            "created_at"
        ]


class PostCommentReplySerializer(serializers.ModelSerializer):
    profile = ProfileInfoSerializer(read_only=True)
    user_liked = serializers.SerializerMethodField()
    user_disliked = serializers.SerializerMethodField()

    def get_user_liked(self, comment):
        request = self.context.get('request', None)
        return comment.likes.filter(id=request.user.profile.id).exists()

    def get_user_disliked(self, comment):
        request = self.context.get('request', None)
        return comment.dislikes.filter(id=request.user.profile.id).exists()

    class Meta:
        model = Reply
        fields = [
            "id",
            "profile",
            "text",
            "user_liked",
            "user_disliked",
            "like_counts",
            "dislike_counts",
            "created_at"
        ]


class AddPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "profile",
            "text",
        ]


class AddPostCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = [
            "id",
            "comment",
            "profile",
            "text",
        ]
