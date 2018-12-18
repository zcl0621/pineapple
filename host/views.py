from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from host.models import PhysicalHost, VirtualHost
from host.serializers import PhysicalHostSerializers, VirtualHostSerializers


# Create your views here.

class PhysicalHostViewSet(viewsets.ModelViewSet):
    queryset = PhysicalHost.objects.all()
    serializer_class = PhysicalHostSerializers
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions,)

    def get_queryset(self):
        queryset = PhysicalHost.objects.all()
        token = self.request.query_params.get('token', None)
        sn = self.request.query_params.get('sn', None)
        user = User.objects.get(id=self.request.user.id)
        if user and token is None and sn is None:
            # 当是页面访问时 没有token和sn
            if user.is_staff:
                return queryset
            else:
                queryset = queryset.filter(datacenter__group__in=user.groups.all())
                return queryset
        elif user and token and sn:
            queryset = queryset.filter(datacenter__token=token, sn=sn)
            return queryset
        elif user and token is None and sn:
            queryset = queryset.filter(sn=sn)
            return queryset
        elif user and token and sn is None:
            queryset = queryset.filter(datacenter__token=token)
            return queryset
        else:
            return None


class VirtualHostViewSet(viewsets.ModelViewSet):
    queryset = VirtualHost.objects.all()
    serializer_class = VirtualHostSerializers
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions,)

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        token = self.request.query_params.get('token', None)
        sn = self.request.query_params.get('sn', None)
        physicalhost = self.request.query_params.get('physicalhost', None)
        queryset = VirtualHost.objects.all()
        if user and token is None and sn is None:
            # 当是页面访问时 没有token和sn
            if user.is_staff:
                return queryset
            else:
                queryset = queryset.filter(datacenter__group__in=user.groups.all())
                return queryset
        elif user and token and sn and physicalhost:
            queryset = queryset.filter(datacenter__token=token, sn=sn, physicalhost=physicalhost)
            return queryset
        elif user and token and sn is None and physicalhost is None:
            queryset = queryset.filter(datacenter__token=token)
            return queryset
        elif user and token is None and sn and physicalhost is None:
            queryset = queryset.filter(sn=sn, physicalhost=physicalhost)
            return queryset
        else:
            return None
