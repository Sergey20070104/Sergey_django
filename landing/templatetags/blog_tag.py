from django import template

register = template.Library()

from ..models import Diary


@register.simple_tag
def total_posts():
    return Diary.objects.count()
