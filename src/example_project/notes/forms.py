from django import forms
from django.core.validators import EmailValidator

from .models import Tag, Note


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class NoteForm(forms.ModelForm):
    files = MultipleFileField(
        required=False,
        label='Файлы',
        widget=MultipleFileInput(attrs={'class': 'form-control'})
    )
    new_tag = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название нового тега'
        }),
        label='Создать новый тег'
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Существующие теги'
    )

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_files(self):
        files = self.files.getlist('files')
        for file in files:
            if file.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError('Размер файла не должен превышать 5MB')

            extension = file.name.split('.')[-1].lower()
            if extension not in ['pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png']:
                raise forms.ValidationError(f'Формат файла .{extension} не поддерживается')
        return files


class NoteEmailForm(forms.Form):
    email = forms.EmailField(
        label='Email получателя',
        validators=[EmailValidator()],
        help_text='Введите email адрес'
    )

    message = forms.CharField(
        label='Дополнительное сообщение',
        required=False,
        help_text='введите сообщение',
    )
