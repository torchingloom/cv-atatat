# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import signals
from config import Config

class User_Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'владелец профиля')

    @staticmethod
    def create(sender, instance, created, **kwargs):
        if created:
            User_Profile.objects.create(user=instance)
            instance.groups.add(Group.objects.get(name=Config.get('users.default_group')))


    def __unicode__(self):
        return u'%s %s (%s)' % (self.user.last_name, self.user.first_name, self.user.username)

    def displayName(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = u'профайл'
        verbose_name_plural = u'профайлы'


signals.post_save.connect(User_Profile.create, sender=User)
