
from django import template
from django.contrib.auth.forms import AuthenticationForm

register = template.Library()

class UserBlock(template.base.Node):
    def render(self, context):
        if template.resolve_variable('user', context).is_authenticated():
            tpl = 'hello_username'
        else:
            tpl = 'login_form'
            context.update({'form': AuthenticationForm()})
        return template.loader.get_template('account/%s.html' % tpl).render(context)

@register.tag
def user_block(parser, token):
    return UserBlock()



