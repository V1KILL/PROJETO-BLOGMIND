import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(value):
    escaped_value = escape(value)
    value = markdown.markdown(escaped_value, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.nl2br'])
    return mark_safe(value)