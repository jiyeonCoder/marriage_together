from rest_framework import serializers
from posts.models import Post, Comment


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "image")


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ("content",)

    """
    def create(self, validated_data):
        author = self.context["author"]
        comment = Comment.objects.create(author=author, **validated_data)
        return comment
    """


class PostSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"