# -*- coding: utf-8 -*-

from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_models

signals.post_syncdb.disconnect(create_superuser, sender=auth_models, dispatch_uid = "django.contrib.auth.management.create_superuser")
#signals.post_syncdb.connect(Init_Data.post_authmodels, sender=auth_models)
