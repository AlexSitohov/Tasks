from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from main.forms import *
from main.models import *


@csrf_exempt
def main_view(request):
    users_objects = User.objects.all()
    if request.method == 'POST' and request.POST.get('user_object_identification') != 'all':
        notes = Note.objects.filter(author=request.POST.get('user_object_identification')).order_by('done',
                                                                                                    '-create_date', )

    elif request.method == 'GET' and request.GET.get('search'):

        notes = Note.objects.filter(title__icontains=request.GET.get('search')).order_by('done', '-create_date', )

    elif request.user.is_authenticated:
        notes_self = list(Note.objects.filter(author=request.user.id).order_by('done', '-create_date', ))
        notes_exclude_self = list(Note.objects.exclude(author=request.user.id).order_by('done', '-create_date', ))
        # notes = Note.objects.all().order_by('author','done', '-create_date', )
        notes = notes_self + notes_exclude_self

    else:
        notes = Note.objects.all().order_by('done', '-create_date', )

    context = {'notes': notes,
               'users_objects': users_objects,
               'title': 'Главная страница'}
    return render(request, 'main/main.html', context)


@csrf_exempt
def self_tasks_view(request):
    notes = Note.objects.filter(author=request.user.id).order_by('done', '-create_date', )
    context = {'notes': notes,

               'title': 'Мои таски'}
    return render(request, 'main/self_tasks.html', context)


@csrf_exempt
def create_task_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateNoteForm(request.POST)  # form не используется. данные приходят из request.POST
            note = Note.objects.create(title=request.POST.get('title'), text=request.POST.get('text'),
                                       done=request.POST.get('done'), hidden=request.POST.get('hidden'),
                                       author=request.user)
            return redirect('main')
        else:
            form = CreateNoteForm()
            context = {'form': form,
                       'title': 'Создать таск'}
        return render(request, 'main/create.html', context)


@csrf_exempt
def update_task_view(request, id):
    try:
        note = Note.objects.get(id=id)
        if note.author == request.user:
            if request.method == 'POST':
                note.title = request.POST.get('title')
                note.text = request.POST.get('text')
                note.done = request.POST.get('done')
                note.hidden = request.POST.get('hidden')
                note.save()
                return redirect('main')
            else:
                context = {'note': note,
                           'title': f'Редактировать таск №{note.id}'}
                return render(request, 'main/update.html', context)
        else:
            return HttpResponse('Отказано в доступе')
    except Exception:
        return HttpResponse('Error')


@csrf_exempt
def delete_task_view(request, id):
    try:
        note = Note.objects.get(id=id)
        if note.author == request.user:
            note.delete()
        else:
            return HttpResponse('Отказано в доступе')
        return redirect('main')

    except Exception:
        pass


@csrf_exempt
def register_account_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main')
        else:
            form = CreateUserForm()
        context = {'form': form, 'title': 'Создать новый аккаунт'}
    else:
        return HttpResponse('Вы уже вошли')
    return render(request, 'main/create_account.html', context)


@csrf_exempt
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


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('main')
