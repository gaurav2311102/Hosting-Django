from django import template

register = template.Library()

def cut(value,args):
    
    return value.replace(args,'')

register.filter('cut',cut)

@register.filter(name='first')
def first(value):
    return value[0]


