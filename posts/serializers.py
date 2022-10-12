from rest_framework import serializers, filters
from posts.models import Post
from likes.models import Like


# Class provided by CI-API walkthrough.
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer Posts Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Restrict size of image.
        Produce error warning to inform user.
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'image hight larger than 4096px!'
            )
            return value

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Return's & calculate's total number
        of likes on post view.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            print('liked')
            return like.id if like else None
        return None

    class Meta:
        """
        Display fields for views.
        """
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
        ]
