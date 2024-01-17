from django import template
from goods.models import Category

register = template.Library()

@register.simple_tag()
def all_categories_tag():
    return Category.objects.all()