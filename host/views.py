from rest_framework import viewsets, permissions

from host.models import Host, HostTag
from host.serializers import HostSerializers, HostTagSerializers
from host.permissions import HostTokenPermission


# Create your views here.


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializers
    permission_classes = (HostTokenPermission, permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        try:
            token = request.data['token']
        except KeyError:
            pass




class HostTagViewSet(viewsets.ModelViewSet):
    queryset = HostTag.objects.all()
    serializer_class = HostTagSerializers
    permission_classes = (permissions.IsAuthenticated,)
