from rest_framework import routers
from churchApp.viewsets import SermonViewSet,CommentViewSet

router = routers.DefaultRouter()

router.register(r'sermon',SermonViewSet)
router.register(r'comments',CommentViewSet)
