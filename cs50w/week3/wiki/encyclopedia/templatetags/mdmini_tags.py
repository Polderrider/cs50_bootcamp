from django import template
from encyclopedia.mdmini import MiniMd


register = template.Library()

_converter = MiniMd()

@register.filter(name='markdown_mini')
def markdown_mini(value: str) -> str:
    return _converter.convert(value or '')