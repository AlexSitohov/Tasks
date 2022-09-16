from django.contrib.admin import *

from main.models import *


@register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ('id', 'author', 'title', 'text', 'done', 'create_date')
    list_display_links = ('title', 'text')
    list_editable = ('done',)
