# templatetags/__init__.py
# Archivo vacío para que Python reconozca el directorio como un paquete

# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='addvalue')
def addclass(field, value):
    return field.as_widget(attrs={'value': value})