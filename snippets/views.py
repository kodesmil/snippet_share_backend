from rest_framework import viewsets, generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnlyCollection, IsOwnerOrReadOnlySnippet, IsOwnerOrReadOnlyComment, IsAdminTag
from .models import Collection, Snippet, Comment, Tag
from .serializers import CollectionSerializer, SnippetSerializer, CommentSerializer, TagSerializer, UserSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyCollection,
                          )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlySnippet,
                          )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnlyComment,
                          )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAdminTag,
                          )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
