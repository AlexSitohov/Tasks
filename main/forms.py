from django.forms import *

from main.models import *


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text', 'done')
