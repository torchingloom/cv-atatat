# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from account.models import User_Profile
from registration.models import RegistrationProfile


class ProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(RegistrationProfile)
admin.site.register(User, UserAdmin)