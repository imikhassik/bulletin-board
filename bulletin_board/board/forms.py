from django import forms

from .models import Post, Attachment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'category',
        ]
        labels = {
            'title': 'Заголовок',
            'body': '',
            'category': 'Категория'
        }
