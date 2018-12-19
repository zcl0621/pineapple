"""pineapple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from datacenter import views as datacenter_views
from host import views as host_views
from public import views as public_views
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'datacenter', datacenter_views.DataCenterViewSet)
router.register(r'physicalhost', host_views.PhysicalHostViewSet)
router.register(r'virtualhost', host_views.VirtualHostViewSet)
router.register(r'public/group', public_views.GroupViewset)
router.register(r'public/permission', public_views.PermissionViewset)
router.register(r'public/user', public_views.UserViewset)
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^auth/', obtain_jwt_token),
]
