from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BaseAuthentication

from datacenter.models import DataCenter


class HostTokenAuthorization(BaseAuthentication):
    def authenticate(self, request):
        # 获取post或者put中的token
        try:
            token = request.data['token']
        except KeyError:
            token = ""
        # 根据token查找user并返回一个tuple
        # 注意是tuple!
        return self.get_datacenter(token), None

    def get_datacenter(self, token):
        try:
            if DataCenter.objects.get(token=token):
                return User.objects.get(pk=1)
        except ObjectDoesNotExist:
            return None

    def authenticate_header(self, request):
        pass
