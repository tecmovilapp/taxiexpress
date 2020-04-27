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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

urlpatterns = [
    # api routes
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/token/$', CustomClaimsTokenObtainPairViewSet.as_view(), name='token_obtain_pair'),
    url(r'^api/v1/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

    # handlers routes
    url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^cars/', include('cars.urls')),
    url(r'^admin/taxiadmin/', include('taxiadmin.urls')),
    url(r'^accounts/', include('core.urls')),
    url(r'^admin/', admin.site.urls),

    url(
        r'^admin/password_reset/$',
        auth_views.PasswordResetView.as_view(template_name='admin/registration/password_reset_form.html'),
        name='admin_password_reset',
    ),
    url(
        r'^admin/password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='admin/registration/password_reset_done.html'),
        name='password_reset_done',
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='admin/registration/password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    url(
        r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='admin/registration/password_reset_complete.html'),
        name='password_reset_complete',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)