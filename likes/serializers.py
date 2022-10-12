from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer model for likes
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'created_at', 'owner', 'post'
        ]

    def create(self, validated_data):
        """
        Throws an error message if
        the user attempt's to like the same
        post more than once.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible Duplicate'
            })
