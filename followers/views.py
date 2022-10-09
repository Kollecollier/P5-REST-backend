from rest_framework import generics, permissions
from p5backend.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer_class = FollowerSerializer
        queryset = Follower.objects.all()
        permission_classes = [permissions.IsOwnerOrReadOnly]


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Delete a new follower if u are the userowner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
