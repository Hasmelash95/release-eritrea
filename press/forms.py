from .models import Comment, Article
from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):
    title = forms.TextInput()
    content = SummernoteTextField()
    excerpt = forms.TextInput()
    slug = forms.TextInput()

    class Meta:
        model = Article
        widgets = {
            'content': SummernoteWidget(),
        }
        fields = ['title', 'content', 'excerpt']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
