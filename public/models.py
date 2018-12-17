from django.db import models
from matplotlib.colors import cnames

# Create your models here.
COLOR_CHOICES = [(name, hex) for name, hex in cnames.items()]


class Tag(models.Model):
    """
    主机标签
    name 标签名
    color 标签颜色
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, null=False)
    color = models.CharField(choices=COLOR_CHOICES, default='yellow', max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name
