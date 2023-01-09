from .models import Comment, Article
from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget
from django.utils.translation import gettext_lazy as _


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title*:', required=True,
                            widget=forms.Textarea(attrs={'rows': 1,
                                                  'cols': 80}))
    content = SummernoteTextField()
    excerpt = forms.CharField(required=False, widget=forms.Textarea(
                              attrs={'rows': 4, 'cols': 80}))
    slug = forms.TextInput()

    class Meta:
        model = Article
        widgets = {
            'content': SummernoteWidget(attrs={'required': True}),
        }
        labels = {
            'content': 'Content*'
        }
        fields = ['title', 'content', 'excerpt', 'tags']


class CommentForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,
                              'cols': 80}))

    class Meta:
        model = Comment
        fields = ['subject', 'content']
