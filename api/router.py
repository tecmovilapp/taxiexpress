from django.conf.urls import url, include
from rest_framework import routers
from api.views.users import UserViewSet
from api.views.groups import GroupViewSet
from api.views.drivers import DriversViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'drivers', DriversViewSet, basename='drivers')
router.register(r'groups', GroupViewSet)

