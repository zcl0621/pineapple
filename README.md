# README
python >= 3.6
pip install -r requirements.txt

# 接口列表
## 登陆
```
/api/login post
{
'username':'xxx',
'password':'xxxx'
}
```
```
request:
    {
    'token':'xxxxxxx'
    }
```

## 用户信息
获取登陆用户信息
```
/api/user/?token get
token=xxxxxxx
```

```
request
```

列表(管理员)
```
/api/user/ get
```

创建(管理员)
```
/api/user post
```

更新
```
/api/user/id put
```

删除
```
/api/user/ delete
```

## 用户组
需要管理员权限

列表
```
/api/group get
```

指定用户组
```
/api/group/id get
```

创建
```
/api/group/ post
```

修改
```
/api/group/ put
```

删除
```
/api/group delete
```

## 数据中心
列表 管理员获取所有 普通用户获取所在组的
```
/api/datacenter get
```

指定数据中心信息
```
/api/datacenter/id get
```

创建
```
/api/datacenter/ post
```

更新
```
/api/datacenter/id put
```

删除
```
/api/datacenter/id delete
```

## 权限
列表
```
/api/permission get
```

获取指定权限
```
/api/permission/id get
```

修改
```
/api/permission/id put
```

删除
```
/api/permission/id delete
```

## 物理主机
获取列表 管理获取所有 普通用户获取所在组
```
/api/physicalhost/ get
```
客户端获取信息
```
/api/physicalhost/ get
token 数据中心token
sn 物理主机的主板号
```

指定物理主机
```
/api/physicalhost/id get
```

创建
```
/api/physicalhost/id post
```

修改
```
/api/physicalhost/id put
```

删除
```
/api/physicalhost/id delete
```

## 虚拟主机
获取列表 管理获取所有 普通用户获取有权限的
```
/api/virtualhost/list
```

指定虚拟主机
```
/api/virtualhost/id get
```

创建
```
/api/virtualhost/id post
```

修改
```
/api/virtualhost/id put
```

删除
```
/api/virtualhost/id delete
```



