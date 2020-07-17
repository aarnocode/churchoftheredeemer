from rest_framework import viewsets
from .models import Sermon
from .serializers import SermonSerializer

class SermonViewSet(viewsets.ModelViewSet):
    queryset=Sermon.objects.all()
    serializer_class=SermonSerializer
