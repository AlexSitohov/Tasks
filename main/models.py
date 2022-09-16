from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import *


class Note(Model):
    CHOICE = (('Сделано', 'Сделано'),
              ('Не cделано', 'Не cделано'))
    author = ForeignKey(User, on_delete=CASCADE, default=None)
    title = CharField('Заголовок', max_length=50)
    text = TextField('Текст')
    done = CharField('Сделано', max_length=20, choices=CHOICE)
    create_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'note'
        verbose_name = 'Таск'
        verbose_name_plural = 'Таски'
