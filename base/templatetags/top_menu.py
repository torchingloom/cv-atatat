# -*- coding: utf-8 -*-

from django import template
from config import Config

register = template.Library()

class TopMenu(template.base.Node):
    context = None

    def render(self, context):
        self.context = context
        context.update({'items': self.items()})
        return template.loader.get_template('base/top_menu.html').render(self.context)

    def items(self):
        user = template.resolve_variable('user', self.context)
        if user.is_authenticated():
            for groupname in Config.get('users.groups'):
                if template.resolve_variable('user', self.context).groups.filter(name=groupname):
                    return Config.get('topmenu/%s' % groupname)
        return Config.get('topmenu/guests')

@register.tag
def top_menu(parser, token):
    return TopMenu()



