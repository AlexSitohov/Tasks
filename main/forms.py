from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from main.models import *


class NoteForm(forms.ModelForm):
    CHOICE = (('Сделано', 'Сделано'),
              ('Не cделано', 'Не cделано'))
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control'}))
    done = forms.TypedChoiceField(label='Сделано', choices=CHOICE,
                                  widget=forms.RadioSelect(attrs={'class': "form-check"}))
    # author = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Note
        fields = ('title', 'text', 'done', 'author')


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
