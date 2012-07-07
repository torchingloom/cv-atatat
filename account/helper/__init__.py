# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

def get_moderators():
    return User.objects.filter(groups__name='moderators')