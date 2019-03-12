# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Archivos'

    def ready(self):
        from core.signals import reset_password_token_created
