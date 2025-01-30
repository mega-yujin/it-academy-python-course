from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View, generic
from django.urls import reverse_lazy, reverse

from .models import Note, Tag
from .forms import NoteForm, NoteModelForm


# def index(request: HttpRequest):
#     context = {
#         'notes': Note.objects.all(),
#     }
#     return render(request, 'index.html', context)

# class HomeView(generic.TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self):
#         return {
#             'notes': Note.objects.all(),
#         }

class HomeView(generic.ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(generic.DetailView):
    model = Note
    context_object_name = 'note'


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy('index')


class AddNoteView(generic.CreateView):
    model = Note
    form_class = NoteModelForm
    template_name = 'notes/add_note.html'
    success_url = reverse_lazy('index')
    # fields = ('title', 'content', 'file', 'tags')

    def form_valid(self, form):
        new_tag_name = form.cleaned_data.get('new_tag')
        if new_tag_name:
            tag, _ = Tag.objects.get_or_create(name=new_tag_name)

        note = form.save(commit=False)
        note.owner_id = 1
        note.save()
        form.save_m2m()

        if new_tag_name:
            note.tags.add(tag)
        return redirect('note_detail', pk=note.pk)


class NoteUpdateView(generic.UpdateView):
    model = Note
    form_class = NoteModelForm
    template_name = 'notes/add_note.html'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

# class AddNoteView(View):
#     def get(self, request: HttpRequest):
#         form = NoteForm()
#         return render(request, 'notes/add_note.html', {'form': form})
#
#     def post(self, request: HttpRequest):
#         form = NoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = Note(
#                 title=form.cleaned_data.get('title'),
#                 content=form.cleaned_data.get('content'),
#                 owner_id=1,
#             )
#             note.save()
#             if tags := form.cleaned_data.get('tags'):
#                 note.tags.set(tags)
#             return redirect('note_detail', pk=note.pk)
#         return render(request, 'notes/add_note.html', {'form': form})

# def add_note(request: HttpRequest):
#     if request.method == 'POST':
#         form_data = request.POST.dict()
#         note = Note(
#             title=form_data.get('title'),
#             content=form_data.get('content'),
#             owner_id=1,
#         )
#         note.save()
#         return redirect('index')
#     return render(request, 'add_note.html')
