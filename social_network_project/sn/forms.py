from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    hashtags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '#django #webdev'}),
        help_text="Separate hashtags with spaces"
    )

    class Meta:
        model = Post
        fields = ['content', 'is_private']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Write a comment...'
        }),
        required=True,
        max_length=500,
    )
