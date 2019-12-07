from snippets.models import Snippet, Comment
from .models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    snippet = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(), allow_null=True)
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), allow_null=True)
    author = serializers.ReadOnlyField(source='author.username')
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        if validated_data['comment'] is not None or validated_data['snippet'] is not None:
            return Report.objects.create(**validated_data)

    class Meta:
        model = Report
        fields = ('id',
                  'is_active',
                  'author',
                  'content',
                  'snippet',
                  'comment'
                  )
