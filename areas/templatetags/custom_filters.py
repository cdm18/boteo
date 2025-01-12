# templatetags/__init__.py
# Archivo vacío para que Python reconozca el directorio como un paquete

# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css_class):
    return field.as_widget(attrs={'class': css_class})