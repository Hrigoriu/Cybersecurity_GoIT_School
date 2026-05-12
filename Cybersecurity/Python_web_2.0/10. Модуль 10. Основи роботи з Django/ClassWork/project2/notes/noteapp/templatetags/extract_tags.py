#notes/noteapp/templatetags/extract_tags.py
from django import template

register = template.Library()

@register.filter(name='tags')
def tags(note_tags):
    return ', '.join([tag.name for tag in note_tags.all()])
