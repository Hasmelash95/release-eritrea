from .models import Comment, Article
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        content = forms.CharField(widget=SummernoteWidget())
        fields = ('title', 'author', 'content', 'excerpt',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
