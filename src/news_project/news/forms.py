from django import forms

from .models import Article, Category, ArticleImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         label='Заголовок',
#         max_length=200,
#         help_text='Краткое название новости',
#         required=True,
#     )
#     content = forms.CharField(
#         label='Содержание новости',
#         help_text='Основной текст новости',
#         required=True,
#     )
#     file = forms.FileField(
#         label='Прикрепить файл',
#         required=False,
#     )
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Category.objects.all(),
#         label='Категории',
#         required=False,
#         help_text='Выберите один или несколько категорий',
#     )
class ArticleModelForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label="Новая категория",
        widget=forms.TextInput(attrs={"placeholder": "Введите новую категорию"})
    )

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Существующие категории'
    )
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Размер изображения не должен превышать 5MB')

            from PIL import Image
            try:
                img = Image.open(image)
                if img.format.lower() not in ['jpeg', 'jpg', 'png', 'gif']:
                    raise forms.ValidationError('Поддерживаются только форматы JPEG, PNG и GIF')

                if img.width < 100 or img.height < 100:
                    raise forms.ValidationError('Изображение слишком маленькое')

            except Exception as e:
                raise forms.ValidationError('Ошибка проверки изображения')

        return image



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            self.save()
        return user

class EmailArticleForm(forms.Form):
    to_email = forms.EmailField(label='Email получателя')
    message = forms.CharField(label='Сообщение', required=False, widget=forms.Textarea)
