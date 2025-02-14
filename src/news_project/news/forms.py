from django import forms
from django.core.validators import EmailValidator
from .models import Article


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_image_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_image_clean(d, initial) for d in data]
        else:
            result = single_image_clean(data, initial)
        return result


class ArticleForm(forms.ModelForm):
    files = MultipleImageField(
        required=False,
        label='Files',
        widget=MultipleFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_files(self):
        files = self.files.getlist('files')
        for file in files:
            if file.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError('Files must be less than 5MB')

            extension = file.name.split('.')[-1].lower()
            if extension not in ['pdf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png']:
                raise forms.ValidationError(f'File format .{extension} is invalid')
        return files


class ArticleEmailForm(forms.Form):
    email = forms.EmailField(
        label='Receiver email',
        validators=[EmailValidator()],
        help_text='Enter email'
    )

    message = forms.CharField(
        label='Additional message',
        required=False,
        help_text='Enter message',
    )
