from django import template
import os

register = template.Library()

@register.filter
def remove(value, argument):
    return value.replace(argument, '-')

@register.filter
def filename(value):
    return os.path.basename(str(value))
