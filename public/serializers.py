from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from rest_framework import serializers

from public.models import Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'created', 'updated')
        read_only_fields = ('created', 'updated')


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class PermissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'content_type', 'codename', 'objects')


class UserSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.is_staff = validated_data['is_staff']
        user.is_active = validated_data['is_active']
        user.save()
        # 这里需要保存下user 否则会出现多联表user不存在id的报错
        for group in validated_data['groups']:
            user.groups.add(group)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.is_staff = validated_data['is_staff']
        instance.is_active = validated_data['is_active']
        instance.save()
        instance.groups.clear()
        for group in validated_data['groups']:
            instance.groups.add(group)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'groups', 'password')
