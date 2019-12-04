from django.contrib.auth.models import User
from .models import Collection, Snippet, Comment, Tag
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Collection
        fields = ('id',
                  'name',
                  'author',
                  'snippets'
                  )


class SnippetSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    collection = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Snippet
        fields = ('id',
                  'name',
                  'code',
                  'stars',
                  'collection',
                  'tags',
                  'comments',
                  )


class CommentSerializer(serializers.ModelSerializer):
    stars = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.username')
    text = serializers.CharField()

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return Comment.objects.create(**validated_data)

    class Meta:
        model = Comment
        fields = ('id',
                  'text',
                  'author',
                  'snippet',
                  'stars',
                  )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id',
                  'name',
                  )


class UserSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'email',
                  'collections',
                  )
