from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from main.models import *


class CreateNoteForm(forms.ModelForm):
    CHOICE = (('Не cделано', 'Не cделано'),
              ('Сделано', 'Сделано'))
    CHOICE_2 = (('Публичная', 'Публичная'),
                ('Приватная', 'Приватная'))
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'id': 'title', 'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'id': 'text', 'class': 'form-control'}),
                           required=False)
    done = forms.TypedChoiceField(label='Сделано', choices=CHOICE,
                                  widget=forms.Select(attrs={'id': 'done', 'class': "form-select"}))
    hidden = forms.TypedChoiceField(label='Приватная запись', choices=CHOICE_2, widget=forms.Select(attrs={'class': "form-select"}))

    class Meta:
        model = Note
        fields = ('title', 'text', 'done', 'hidden')


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
