import markdown
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(value):

    value = value.replace('\n', '<br>')
    # Converte Markdown para HTML
    value = markdown.markdown(value)
    return value