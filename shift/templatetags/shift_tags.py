from django import template

register = template.Library()


@register.simple_tag()
def sorting(**kwargs):
    url = kwargs["url"]
    sorting_field = kwargs["sorting_field"]
    direction = kwargs["direction"]
    sorted_get_request = f"sorting_field={sorting_field}&direction={direction}"
    sorted_url = f"{url}?{sorted_get_request}"
    return sorted_url
