from .models import Comment
from rest_framework import serializers


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
