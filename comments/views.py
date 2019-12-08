from rest_framework import viewsets, generics, permissions
from comments.models import Comment
from comments.permissions import IsOwnerOrReadOnlyComment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyComment,
                          )
