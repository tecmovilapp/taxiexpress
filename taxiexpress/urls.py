"""taxiexpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from api.router import router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import CustomClaimsTokenObtainPairViewSet


urlpatterns = [
    # api routes
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/token/$', CustomClaimsTokenObtainPairViewSet.as_view(), name='token_obtain_pair'),
    url(r'^api/v1/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/v1/pwreset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # handlers routes
    url(r'^cars/', include('cars.urls')),
    url(r'^admin/taxiadmin/', include('taxiadmin.urls')),
    url(r'^accounts/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]