from django.contrib.auth.models import User

from django.db.models import *


class Note(Model):
    CHOICE = (('Сделано', 'Сделано'),
              ('Не cделано', 'Не cделано'))
    CHOICE_2 = (('Публичная', 'Публичная'),
                ('Приватная', 'Приватная'))
    author = ForeignKey(User, on_delete=CASCADE, default=None)
    title = CharField('Заголовок', max_length=50)
    text = TextField('Текст', blank=True)
    done = CharField('Сделано', max_length=20, choices=CHOICE)
    create_date = DateTimeField('Дата создания', auto_now_add=True)
    hidden = CharField('Приватная запись', max_length=20, choices=CHOICE_2, default='Публичная', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'note'
        verbose_name = 'Таск'
        verbose_name_plural = 'Таски'
