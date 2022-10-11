from django import template

register = template.Library()

@register.simple_tag()
def sorting(**kwargs):
    pole = kwargs['pole']
    asc = kwargs['asc']
    if asc is True:
        sorted_url = f"pole={pole}&asc=True"
        return sorted_url
    else:
        sorted_url = f"pole={pole}&asc=False"
        return sorted_url
