from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserCreateAPIView

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
    path('create', UserCreateAPIView.as_view(), name='create')
]