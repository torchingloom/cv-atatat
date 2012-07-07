# -*- coding: utf-8 -*-

from django import template
from config import Config
from base.models import Dashboard


register = template.Library()

class DashboardMenu(template.base.Node):
    context = None

    def render(self, context):
        self.context = context
        self.context['data'] = Dashboard(self.context['request'].user)
        self.context['items'] = self.items()
        return template.loader.get_template('base/dashboard/menu.html').render(self.context)

    def items(self):
        items = Config.get('dashboard-menu/%s' % self.context['data'].user_groupname)
        for item in items:
            if self.context['request'].path == item['url']:
                item['active'] = True
            if item.has_key('counter_name'):
                item['counter'] = getattr(self.context['data'], item['counter_name'])
        return items

@register.tag
def dashboard_menu(parser, token):
    return DashboardMenu()



