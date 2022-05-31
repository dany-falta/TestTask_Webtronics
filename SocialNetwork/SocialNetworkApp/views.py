from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet

from .serializers import UserRegisterSerializer, PostSerializer
from .models import Post


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    


class PostViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }

    @action(detail=True, methods=['post'])
    def like(self):
        post = self.get_object()
        post.likes.add(self.request.user)
        return Response(status=HTTP_201_CREATED)

    @like.mapping.delete
    def unlike(self):
        post = self.get_object()
        post.likes.remove(self.request.user)
        return Response(status=HTTP_204_NO_CONTENT)