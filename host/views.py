from rest_framework import viewsets, permissions

from host.models import PhysicalHost, VirtualHost, HardwareInfo
from host.serializers import PhysicalHostSerializers, VirtualHostSerializers, HardwareInfoSerializers
from host.permissions import HostTokenPermission


# Create your views here.


class PhysicalHostViewSet(viewsets.ModelViewSet):
    queryset = PhysicalHost.objects.all().order_by('-id')
    serializer_class = PhysicalHostSerializers
    permission_classes = (HostTokenPermission, permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = PhysicalHost.objects.all()
        token = self.request.query_params.get('token', None)
        sn = self.request.query_params.get('sn', None)
        if token and sn:
            queryset = queryset.filter(datacenter__token=token, sn=sn)
        elif sn:
            queryset = queryset.filter(sn=sn)
        elif token:
            queryset = queryset.filter(datacenter__token=token)
        return queryset


class VirtualHostViewSet(viewsets.ModelViewSet):
    queryset = VirtualHost.objects.all().order_by('-id')
    serializer_class = VirtualHostSerializers
    permission_classes = (HostTokenPermission, permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = VirtualHost.objects.all()
        token = self.request.query_params.get('token', None)
        sn = self.request.query_params.get('sn', None)
        physicalhost = self.request.query_params.get('physicalhost', None)
        if token and sn and physicalhost:
            queryset = queryset.filter(datacenter__token=token, sn=sn, physicalhost=physicalhost)
        elif token:
            queryset = queryset.filter(datacenter__token=token)
        elif sn and physicalhost:
            queryset = queryset.filter(sn=sn, physicalhost=physicalhost)
        return queryset
