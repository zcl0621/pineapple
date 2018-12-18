from django.db import models
from django.contrib.auth.models import Group


# Create your models here.

class DataCenter(models.Model):
    """
    name 数据中心名
    site 数据中心位置
    contact 数据中心联系人
    phone 数据中心联系人电话
    email 数据中心联系人邮箱
    other_info 数据中心其他信息
    toekn 主机信息 api token值
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, null=False)
    site = models.CharField(max_length=256, null=False)
    contact = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=11, null=False)
    email = models.EmailField(null=False)
    other_info = models.TextField(null=True)
    token = models.TextField(null=False)
    group = models.ManyToManyField(to=Group)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'datacenter'

    def __str__(self):
        return self.name
