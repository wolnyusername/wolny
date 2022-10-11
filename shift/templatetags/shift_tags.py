from django import template

register = template.Library()

@register.simple_tag()
def sorting(**kwargs):
    url = kwargs['url']
    pole = kwargs['pole']
    asc = kwargs['direction']
    if asc is True:
        sorted_url = url+pole+'?true'
        return sorted_url
    else:
        sorted_url = url+pole+'?flase'
        return sorted_url
