from django.conf.urls import url, include
from rest_framework import routers
from api.views.users import UserViewSet
from api.views.groups import GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

