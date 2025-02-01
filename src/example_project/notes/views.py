from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Note, Tag
from .forms import NoteForm, NoteModelForm, UserRegistrationForm


@login_required
def index(request: HttpRequest):
    context = {
        'notes': Note.objects.all(),
    }
    return render(request, 'index.html', context)


# class HomeView(generic.TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self):
#         return {
#             'notes': Note.objects.all(),
#         }

class HomeView(LoginRequiredMixin, generic.ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.prefetch_related('tags').filter(owner=self.request.user)


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    context_object_name = 'note'


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    success_url = reverse_lazy('index')


class AddNoteView(LoginRequiredMixin, generic.CreateView):
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
        note.owner = self.request.user
        note.save()
        form.save_m2m()

        if new_tag_name:
            note.tags.add(tag)
        return redirect('note_detail', pk=note.pk)


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteModelForm
    template_name = 'notes/add_note.html'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})


class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, owner=self.request.user)
        note.is_favorite = not note.is_favorite
        note.save()
        return redirect('index')


class FavoriteNotesView(LoginRequiredMixin, generic.ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.prefetch_related('tags').filter(
            Q(owner=self.request.user) & Q(is_favorite=True)
        )
