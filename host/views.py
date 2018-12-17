from rest_framework import viewsets, permissions

from host.models import PhysicalHost, VirtualHost, HardwareInfo
from host.serializers import PhysicalHostSerializers, VirtualHostSerializers, HardwareInfoSerializers
from host.permissions import HostTokenPermission


# Create your views here.


class PhysicalHostViewSet(viewsets.ModelViewSet):
    queryset = PhysicalHost.objects.all()
    serializer_class = PhysicalHostSerializers
    permission_classes = (permissions.IsAuthenticated,)


class VirtualHostViewSet(viewsets.ModelViewSet):
    queryset = VirtualHost.objects.all()
    serializer_class = VirtualHostSerializers
    permission_classes = (permissions.IsAuthenticated,)


class HardwareInfoViewSet(viewsets.ModelViewSet):
    queryset = HardwareInfo.objects.all()
    serializer_class = HardwareInfoSerializers
    permission_classes = (permissions.IsAuthenticated,)
