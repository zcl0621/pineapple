from rest_framework.permissions import BasePermission

from datacenter.models import DataCenter


class HostTokenPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.data['token']
        if DataCenter.objects.get(token=token):
            return True
