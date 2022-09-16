from django.contrib.auth import login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from main.forms import *
from main.models import *


# .order_by('-create_date').values()

def main_view(request):
    notes = Note.objects.filter(author=request.user.id)
    context = {'notes': notes,
               'title': 'Главная страница'}
    return render(request, 'main/main.html', context)


def create_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        form.author = str(request.user.username)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return HttpResponse('error')

    else:
        form = NoteForm()
        context = {'form': form,
                   'title': 'Создать таск'}
        return render(request, 'main/create.html', context)


def update_view(request, id):
    try:
        note = Note.objects.get(id=id)
        if request.method == 'POST':
            note.title = request.POST.get('title')
            note.text = request.POST.get('text')
            note.done = request.POST.get('done')
            note.save()
            return redirect('main')
        else:
            context = {'note': note,
                       'title': f'Редактировать таск №{note.id}'}
            return render(request, 'main/update.html', context)
    except Exception:
        pass


def delete_view(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('main')

    except Exception:
        pass


def create_account_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = CreateUserForm()
    context = {'form': form, 'title': 'Создать новый аккаунт'}
    return render(request, 'main/create_account.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse('Error')

    else:
        form = UserLoginForm
        context = {
            'form': form,
            'title': 'Авторизация'
        }
        return render(request, 'main/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('main')
