from django import template

register = template.Library()

@register.simple_tag()
def sorting(**kwargs):
    url = kwargs['url']
    sorting_field = kwargs['sorting_field']
    direction = kwargs['direction']
    if direction == 'asc':
        sorted_url = f"url={url}&sorting_field={sorting_field}&direction=asc"
        return sorted_url
    else:
        sorted_url = f"url={url}&sorting_field={sorting_field}&direction=desc"
        return sorted_url
