
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.custom_admin_view, name='custom_admin'),
]