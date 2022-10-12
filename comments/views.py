from rest_framework import generics, permissions
from p5backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Class provided by CI-API walkthrough.
class CommentList(generics.ListCreateAPIView):
    """
    Creating and retreiving comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Save comment to user details.
        If user is authenticated."
        """
        serializer.save(owner=self.request.user)

        filter_backends = [
            DjangoFilterBackend,
        ]

        filterset_fields = [
            'post'
        ]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Crud for comments.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
