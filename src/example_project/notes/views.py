from django.http import HttpRequest
from django.shortcuts import render, redirect

from notes.storage import NOTES_STORAGE
from notes.dto_models import Note
from uuid import UUID, uuid4


def index(request: HttpRequest):
    context = {
        'notes': NOTES_STORAGE.values(),
    }
    return render(request, 'index.html', context)


def add_note(request: HttpRequest):
    if request.method == 'POST':
        form_data = request.POST.dict()
        note = Note(
            id=uuid4(),
            title=form_data.get('title'),
            content=form_data.get('content')
        )
        NOTES_STORAGE[note.id] = note
        return redirect('index')
    return render(request, 'add_note.html')

    # if request.method == 'POST':
    #     title = request.form.get('title')
    #     content = request.form.get('content')
    #     note = Note(
    #         id=uuid4(),
    #         title=title,
    #         content=content,
    #         created_at = datetime.now(),
    #     )
    #     db.add_note(note)
    #     return redirect(url_for('index'))
    # return render_template('add_note.html')
