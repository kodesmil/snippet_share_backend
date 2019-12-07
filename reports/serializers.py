from .models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    snippet = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    author = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        if validated_data['comment'] is not None or validated_data['snippet'] is not None:
            return Report.objects.create(**validated_data)

    class Meta:
        model = Report
        fields = ('id',
                  'is_active',
                  'content',
                  'snippet',
                  'comment'
                  )
