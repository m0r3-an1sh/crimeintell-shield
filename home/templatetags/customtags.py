from django import template

register = template.Library()
from home.models import Blog

@register.simple_tag
def murdercount(category):
    murcount = Blog.objects.filter(slug=(category=="MURDER")).all().count()
    return 