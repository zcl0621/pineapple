from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from public.serializers import GroupSerializers, PermissionSerializers, UserSerializers


# Create your views here.

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = (permissions.IsAdminUser, permissions.DjangoModelPermissions, )


class PermissionViewset(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializers
    permission_classes = (permissions.IsAdminUser, permissions.DjangoModelPermissions,)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissions,)

    def get_queryset(self):
        queryset = User.objects.all()
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.filter(username=self.request.user)
