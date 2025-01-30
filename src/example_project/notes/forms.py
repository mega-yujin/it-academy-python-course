from django import forms

from .models import Note, Tag


class NoteForm(forms.Form):
    title = forms.CharField(
        label='Заголовок',
        max_length=200,
        help_text='Краткое название заметки',
        required=True,
    )
    content = forms.CharField(
        label='Содержание заметки',
        help_text='Основной текст заметки',
        required=True,
    )
    file = forms.FileField(
        label='Прикрепить файл',
        required=False,
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        label='Теги',
        required=False,
        help_text='Выберите один или несколько тегов',
    )


class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'file', 'tags']

    new_tag = forms.CharField(
        required=False,
        label='Добавить новый тег',
        # widget=forms.TextInput(
        #     attrs={
        #         'class': 'form-control',
        #     }
        # )
    )
