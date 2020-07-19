from rest_framework import serializers
from .models import Sermon,Comment

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sermon
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        reply_id=serializers.IntegerField(required=False)
