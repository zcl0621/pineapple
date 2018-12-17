from django.db import models
from datacenter.models import DataCenter


# Create your models here.
class HardwareInfo(models.Model):
    """
    ip 主机ip {
            "物理网卡名":{
                "IP_NETMASK_GATEWAY(IP/子网掩码/网关)":"['xxx.xxx.xxx.xxx/24/gateway','xxx.xxx.xxx.xxx/24/gateway']",
                "product_name":"intel"}
            }

    DNS dns地址 ["1.1.1.1","2.2.2.2"]
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
    """
    id = models.AutoField(primary_key=True)
    ip = models.TextField(null=True)
    dns = models.TextField(null=True)
    cpu = models.TextField(null=True)
    memory = models.TextField(null=True)
    disk = models.TextField(null=True)
    gpu = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hardwareinfo'


class PhysicalHost(models.Model):
    """
    hostname 主机名
    purchase 购买时间
    service 维保时长
    machine_room 机房
    cabinet 机柜号
    sn 主板sn号 主机唯一标示
    datacenter 关联datacenter
    """
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=256, null=False)
    service = models.TextField(null=True)
    machine_room = models.TextField(null=True)
    cabinet = models.TextField(null=True)
    sn = models.CharField(max_length=256)
    datacenter = models.ForeignKey(to=DataCenter, on_delete=models.CASCADE)
    hardwareinfo = models.ForeignKey(to=HardwareInfo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'physicalhost'

    def __str__(self):
        return self.hostname


class VirtualHost(models.Model):
    """
    hostname 主机名
    datacenter 关联datacenter
    """
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=256, null=False)
    datacenter = models.ForeignKey(to=DataCenter, on_delete=models.CASCADE)
    hardwareinfo = models.ForeignKey(to=HardwareInfo, on_delete=models.CASCADE)
    sn = models.CharField(max_length=256, null=False)
    physicalhost = models.ForeignKey(to=PhysicalHost, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'virtualhost'

    def __str__(self):
        return self.hostname
