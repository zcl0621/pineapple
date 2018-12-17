from rest_framework import viewsets, permissions

from datacenter.models import DataCenter
from datacenter.serializers import DateCanterSerializers


# Create your views here.


class DataCenterViewSet(viewsets.ModelViewSet):
    queryset = DataCenter.objects.all()
    serializer_class = DateCanterSerializers
    permission_classes = (permissions.IsAuthenticated,)


