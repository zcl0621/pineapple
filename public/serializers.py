from rest_framework import serializers
from public.models import Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'created', 'updated')
        read_only_fields = ('created', 'updated')
