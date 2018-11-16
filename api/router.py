from django.conf.urls import url, include
from rest_framework import routers
from api.views.users import UserViewSet
from api.views.groups import GroupViewSet
from api.views.vehicles import DriverVehiclesViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'users/{pk}/vehicles', DriverVehiclesViewSet)
router.register(r'groups', GroupViewSet)

