
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^rides/$', views.rides_admin_view),
    url(r'^rides/add', views.form_handle, name='form_handle'),
    url(r'^locations', views.locations_view),
]