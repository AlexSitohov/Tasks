from django.shortcuts import render, redirect

# Create your views here.
from main.forms import *
from main.models import *


def main_view(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'main/main.html', context)


def create_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = NoteForm()
        context = {'form': form}
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
            context = {'note': note}
            return render(request, 'main/update.html', context)
    except Exception:
        pass


def update_done_view(request, id):
    if request.method == "POST":
        note = Note.objects.get(id=id)
        note.done = request.POST.get("done")
        note.save()
    return redirect('main')


def delete_view(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('main')

    except Exception:
        pass


def personal_area_view(request, user):
    context = {'user': user}
    return render(request, 'main/personal_area.html', context)
