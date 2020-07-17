from rest_framework import routers
from churchApp.viewsets import SermonViewSet

router = routers.DefaultRouter()

router.register(r'sermon',SermonViewSet)
