from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import GroupSerializer, UserSerializer, CarSerializer, CommentSerializer
from .models import Car, Comment
from .permissions import IsOwnerOrReadOnly, CreateOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(methods=['GET'], detail=True, serializer_class=CommentSerializer,
            permission_classes=[CreateOrReadOnly])
    def comments(self, request, pk=None):
        comments = Comment.objects.all() if not pk else Comment.objects.filter(car=pk)
        comments = CommentSerializer(comments, many=True).data
        return Response({'comments': comments})

    @comments.mapping.post
    def add_comment(self, request, pk=None):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'comments': serializer.data})
        return Response({'detail': serializer.errors})
