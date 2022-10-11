from django import template

register = template.Library()

@register.simple_tag()
def sorting(**kwargs):
    url = kwargs['url']
    sorting_field = kwargs['sorting_field']
    asc = kwargs['asc']
    if asc is True:
        sorted_url = f"{url}&sorting_field={sorting_field}&asc=True"
        return sorted_url
    else:
        sorted_url = f"{url}&sorting_field={sorting_field}&asc=False"
        return sorted_url
