from rest_framework import serializers
from host.models import PhysicalHost, HostTag


# Create your serializers here.


class PhysicalHostSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysicalHost
        fields = (
            'id', 'hostname', 'ip', 'cpu', 'memory', 'motherboard', 'disk', 'gpu', 'dns', 'virtual_host',
            'physical_host',
            'service', 'machine_room', 'cabinet', 'datacenter', 'created', 'updated')
        read_only_fields = ('created', 'updated')


class HostTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = HostTag
        fields = ('id', 'name', 'color', 'host_list', 'datacenter', 'created', 'updated')
        read_only_fields = ('created', 'updated')
