# -*- coding: utf-8 -*-

from django import forms
from extra_views.advanced import InlineFormSet
from registration.forms import RegistrationForm
from models import *





class RegistrationForm(RegistrationForm):
    username = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_username(self):
        return self.cleaned_data['username']

    def clean(self):
        if not self.errors:
            self.cleaned_data['username'] = '%s%s' % (self.cleaned_data['email'].split('@',1)[0], User.objects.count())
        super(RegistrationForm, self).clean()
        return self.cleaned_data




class ProfileInlineForm(InlineFormSet):
    model = User_Profile
    can_delete = False
    extra = 1

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('username', 'password', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')



