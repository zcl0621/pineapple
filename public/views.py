from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from rest_framework import viewsets, permissions

from public.serializers import GroupSerializers, PermissionSerializers, UserSerializers


# Create your views here.

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly,)


class PermissionViewset(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializers
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly,)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticatedOrReadOnly,)
