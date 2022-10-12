from rest_framework import generics, permissions
from p5backend.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    Provide logged in users the ability
    to like/unlike a post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        If the user is authenticated, like/dislike
        will be saved to database
        """
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Crud for Likes
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
