from django.contrib.auth import login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from main.forms import *
from main.models import *


# .order_by('-create_date').values()
def main_view(request):
    u = User.objects.all()
    if request.method == 'POST' and request.POST.get('iii') != 'all':
        notes = Note.objects.filter(author=request.POST.get('iii')).order_by('-create_date')
    else:
        notes = Note.objects.all().order_by('-create_date')
    context = {'notes': notes,
               'u': u,
               'title': 'Главная страница'}
    return render(request, 'main/main.html', context)


def self_tasks_view(request):
    notes = Note.objects.filter(author=request.user.id).order_by('-create_date').values()
    context = {'notes': notes,

               'title': 'Мои таски'}
    return render(request, 'main/self_tasks.html', context)


def create_view(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        note = Note.objects.create(title=request.POST.get('title'), text=request.POST.get('text'),
                                   done=request.POST.get('done'), author=request.user)
        # form.author = request.user

        # if form.is_valid():
        #     form.save()
        return redirect('main')
    # else:
    #     return HttpResponse('error')

    else:
        form = CreateNoteForm()
        context = {'form': form,
                   'title': 'Создать таск'}
    return render(request, 'main/create.html', context)


def update_view(request, id):
    try:
        note = Note.objects.get(id=id)
        if request.method == 'POST' and note.author == request.user:
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
        return HttpResponse('Error')


def delete_view(request, id):
    try:
        note = Note.objects.get(id=id)
        if note.author == request.user:
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
