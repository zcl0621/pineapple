from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from host.models import PhysicalHost, HardwareInfo, VirtualHost


# Create your serializers here.
class HardwareInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HardwareInfo
        fields = ('id', 'ip', 'dns', 'cpu', 'memory', 'disk', 'gpu', 'updated', 'created')
        read_only_fields = ('updated', 'created')


class PhysicalHostSerializers(WritableNestedModelSerializer):
    hardwareinfo = HardwareInfoSerializers(many=False)

    class Meta:
        model = PhysicalHost
        fields = (
            'id', 'hostname', 'service', 'machine_room', 'cabinet', 'sn', 'datacenter', 'hardwareinfo', 'created',
            'updated')
        read_only_fields = ('created', 'updated')


class VirtualHostSerializers(WritableNestedModelSerializer):
    hardwareinfo = HardwareInfoSerializers(many=False)

    class Meta:
        model = VirtualHost
        fields = (
            'id', 'hostname', 'sn', 'datacenter', 'hardwareinfo', 'created',
            'updated', 'physicalhost')
        read_only_fields = ('created', 'updated')
