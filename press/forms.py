from .models import Comment, Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'author', 'content', 'excerpt',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
