from django.contrib.admin import *

from main.models import *


@register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ('id', 'author', 'title', 'done', 'hidden', 'create_date')
    list_display_links = ('title', )
    list_editable = ('done', 'hidden')
