from django.db import models
from datacenter.models import DataCenter
from matplotlib.colors import cnames

# Create your models here.
COLOR_CHOICES = [(name, hex) for name, hex in cnames.items()]


class PhysicalHost(models.Model):
    """
    hostname 主机名
    ip 主机ip {
            "物理网卡名":{
                "IP_NETMASK_GATEWAY(IP/子网掩码/网关)":["xxx.xxx.xxx.xxx/24/gateway","xxx.xxx.xxx.xxx/24/gateway"]
                "product_name":"intel"}
            }
    cpu cpu信息 { "id(物理cpu)": {
            "MODEL_NAME":"Intel(R) Xeon(R) CPU E5-2630",
            "FREQUENCY":"2.4",
            "CORE_NUM(物理核数)":"8",
            "THREAD_NUM(物理线程数)": "16"}
    }
    memory 内存 {
            "id(物理插槽)": {
                "SIZE(大小)":"16384",
                "SPEED(频率)":"2133",
                "Manufacturer(生产厂家)":"Samsung",
                "SN":"4057765F",
                "TYPE(类型)":"DDR4"}
            }
    motherboard 主板 {
            "PRODUCT_NAME(厂家)":"TYAN",
            "SN":"xxxxxxxxxx",
            }
    disk 硬盘 {
            "1(编号)": {
            "SYSTEM_PATH(系统路径)":"/dev/sda",
            "SIZE(总大小)":"512",
            "DISK_PARTITION(分区信息)":{
                "PARTITION_SYSTEM_PATH(分区系统路径)":"/dev/sda1",
                "MOUNT_PATH(挂载点)":"/",
                "SIZE(分区大小)":"60",
                "FORMAT(磁盘格式)":"ext4",
            }}
        }
    gpu 显卡信息 {
            "1":{
            "PRODUCT_NAME":"nvidia",
            "GPU_MEMORY":"8",
            "GPU_PRODUCT":"GTX 1080"}
        }
    DNS dns地址 ["1.1.1.1","2.2.2.2"]
    不是虚拟机
    purchase 购买时间
    service 维保时长
    machine_room 机房
    cabinet 机柜号
    datacenter 关联datacenter
    """
    hostname = models.CharField(max_length=256, null=False)
    ip = models.TextField(null=True)
    cpu = models.TextField(null=True)
    memory = models.TextField(null=True)
    motherboard = models.TextField(null=True)
    disk = models.TextField(null=True)
    gpu = models.TextField(null=True)
    dns = models.TextField(null=True)
    service = models.TextField(null=True)
    machine_room = models.TextField(null=True)
    cabinet = models.TextField(null=True)
    datacenter = models.ForeignKey(to=DataCenter, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'physicalhost'

    def __str__(self):
        return self.hostname


class VirtualHost(models.Model):
    """
    hostname 主机名
    ip 主机ip {
            "物理网卡名":{
                "IP_NETMASK_GATEWAY(IP/子网掩码/网关)":["xxx.xxx.xxx.xxx/24/gateway","xxx.xxx.xxx.xxx/24/gateway"]
                "product_name":"intel"}
            }
    cpu cpu信息 { "id(物理cpu)": {
            "MODEL_NAME":"Intel(R) Xeon(R) CPU E5-2630",
            "FREQUENCY":"2.4",
            "CORE_NUM(物理核数)":"8",
            "THREAD_NUM(物理线程数)": "16"}
    }
    memory 内存 {
            "id(物理插槽)": {
                "SIZE(大小)":"16384",
                "SPEED(频率)":"2133",
                "Manufacturer(生产厂家)":"Samsung",
                "SN":"4057765F",
                "TYPE(类型)":"DDR4"}
            }
    motherboard 主板 {
            "PRODUCT_NAME(厂家)":"TYAN",
            "SN":"xxxxxxxxxx",
            }
    disk 硬盘 {
            "1(编号)": {
            "SYSTEM_PATH(系统路径)":"/dev/sda",
            "SIZE(总大小)":"512",
            "DISK_PARTITION(分区信息)":{
                "PARTITION_SYSTEM_PATH(分区系统路径)":"/dev/sda1",
                "MOUNT_PATH(挂载点)":"/",
                "SIZE(分区大小)":"60",
                "FORMAT(磁盘格式)":"ext4",
            }}
        }
    gpu 显卡信息 {
            "1":{
            "PRODUCT_NAME":"nvidia",
            "GPU_MEMORY":"8",
            "GPU_PRODUCT":"GTX 1080"}
        }
    DNS dns地址 ["1.1.1.1","2.2.2.2"]
    datacenter 关联datacenter
    """
    hostname = models.CharField(max_length=256, null=False)
    ip = models.TextField(null=True)
    cpu = models.TextField(null=True)
    memory = models.TextField(null=True)
    motherboard = models.TextField(null=True)
    disk = models.TextField(null=True)
    gpu = models.TextField(null=True)
    dns = models.TextField(null=True)
    datacenter = models.ForeignKey(to=DataCenter, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'virtualhost'

    def __str__(self):
        return self.hostname

class HostTag(models.Model):
    """
    主机标签
    name 标签名
    color 标签颜色
    host_list 主机列表 list
    datacenter 关联数据中心
    """
    name = models.CharField(max_length=10, null=False)
    color = models.CharField(choices=COLOR_CHOICES, default='yellow', max_length=100, null=False)
    host_list = models.TextField(null=True)
    datacenter = models.ForeignKey(to=DataCenter, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hosttag'

    def __str__(self):
        return self.name
