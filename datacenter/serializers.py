from rest_framework import serializers
from datacenter.models import DataCenter


# Create your serializers here.

class DateCanterSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataCenter
        fields = (
            'id', 'name', 'site', 'contact', 'phone', 'email', 'other_info', 'created', 'updated', 'token', 'group')
        read_only_fields = ('created', 'updated')
