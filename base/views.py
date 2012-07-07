# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from models import *

class Index(TemplateView):
    template_name = 'base/index.html'


class PageView(DetailView):
    model = StaticPage
    template_name = 'base/page/view.html'

class TestEmail(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        from django.contrib.auth.models import User
        from base.helper.mail import ToUsers
        from django.db.models.query_utils import Q
        m = ToUsers(User.objects.filter(Q(id=1) | Q(id=8)), 'test')
        m.send()