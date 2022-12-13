from .models import Comment, Article
from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 80}))
    content = SummernoteTextField()
    excerpt = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 
                              'cols': 80}))
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
