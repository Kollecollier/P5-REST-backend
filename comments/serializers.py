from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Class provided by CI-API walkthrough.

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Associate comment to user ID.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Display's the time passsed since comment was created.
         """
        return naturaltime(obj.created_on)

    def get_modified_on(self, obj):
        """
        Display's the time passsed since comment was modified.
        """
        return naturaltime(obj.modified_on)

    class Meta:
        """
        Return fields to display
        """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for comments detail views.
    """
    post = serializers.ReadOnlyField(source='post.id')
