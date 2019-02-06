from django import template
from my_site.settings import STATIC_URL
register = template.Library()


@register.simple_tag(name='img_address')
def img_address(category, file):

    return STATIC_URL + 'myapp' + '/' + 'images' + '/' + category + '/' + file
