from django.http import HttpRequest, HttpResponseForbidden, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import NoteForm
from .models import Note, Tag, NoteFile


class HomeView(LoginRequiredMixin, generic.ListView):
    model = Note
    context_object_name = 'notes'
    paginate_by = 9
    ordering = ['-created_at']

    def get_queryset(self):
        return Note.objects.prefetch_related('tags').filter(owner=self.request.user)


class FavoritesView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    generic.ListView,
):
    model = Note
    context_object_name = 'notes'
    ordering = ['-created_at']
    permission_required = 'notes.can_mark_as_fav'

    def get_queryset(self):
        return Note.objects.prefetch_related('tags').filter(
            Q(owner=self.request.user) & Q(is_favorite=True)
        )

    def handle_no_permission(self):
        return HttpResponseForbidden("You shall not pass!!")


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    context_object_name = 'note'

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).prefetch_related('files')


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('index')


class AddNoteView(LoginRequiredMixin, generic.CreateView):
    # model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Сохраняем заметку
        note = form.save(commit=False)
        note.owner = self.request.user
        note.save()
        form.save_m2m()

        # поверяем теги
        new_tag_name = form.cleaned_data.get('new_tag')
        if new_tag_name:
            tag, created = Tag.objects.get_or_create(
                name=new_tag_name,
            )

        # Добавление нового тега к заметке
        if new_tag_name:
            note.tags.add(tag)

        # Обрабатываем загруженные файлы
        files = self.request.FILES.getlist('files')
        for file in files:
            NoteFile.objects.create(
                note=note,
                file=file,
            )

        return redirect('note_detail', pk=note.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_tags'] = Tag.objects.exists()
        return context


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_form.html'

    def get_queryset(self):
        # Пользователь может редактировать только свои заметки
        return Note.objects.filter(owner=self.request.user)

    def form_valid(self, form):

        # Обрабатываем новые теги
        new_tag_name = form.cleaned_data.get('new_tag')
        if new_tag_name:
            tag, created = Tag.objects.get_or_create(
                name=new_tag_name,
            )
            self.object.tags.add(tag)

        # Обрабатываем новые файлы
        files = self.request.FILES.getlist('files')
        for file in files:
            NoteFile.objects.create(
                note=self.object,
                file=file,
            )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_tags'] = Tag.objects.exists()
        return context


class ToggleFavoriteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'notes.can_mark_as_fav'

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, owner=self.request.user)
        note.is_favorite = not note.is_favorite
        note.save()
        return redirect('index')


@login_required
def delete_note_file(request, note_pk, pk):
    note = get_object_or_404(Note, pk=note_pk, owner=request.user)
    file = get_object_or_404(NoteFile, pk=pk, note=note)
    file.delete()
    messages.success(request, 'Файл удален')
    return redirect('note_update', pk=note_pk)
