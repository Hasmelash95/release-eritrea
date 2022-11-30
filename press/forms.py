from .models import Comment, Article
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ArticleForm(forms.ModelForm):
    title = forms.TextInput()
    content = forms.TextInput()
    excerpt = forms.TextInput()
    slug = forms.TextInput()

    class Meta:
        model = Article
        fields = ['title', 'content', 'excerpt']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
