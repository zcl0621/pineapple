from rest_framework import viewsets, permissions

from datacenter.models import DataCenter
from datacenter.serializers import DateCanterSerializers
from django.contrib.auth.models import User


# Create your views here.


class DataCenterViewSet(viewsets.ModelViewSet):
    queryset = DataCenter.objects.all()
    serializer_class = DateCanterSerializers
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAuthenticated,)

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        if user.is_staff:
            queryset = DataCenter.objects.all()
        else:
            queryset = DataCenter.objects.filter(group__in=user.groups.all())
        return queryset
