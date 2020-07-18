from rest_framework import viewsets
from .models import Sermon,Comment
from .serializers import SermonSerializer,CommentSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset=Sermon.objects.all()
    serializer_class=SermonSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
