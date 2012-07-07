
from django import template

register = template.Library()

@register.filter
def profile_url(user):
    return '/profile/view/%s' % (user.id)



