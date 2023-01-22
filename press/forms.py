from .models import Comment, Article
from django import forms
from django_summernote.fields import SummernoteWidget, SummernoteTextField
from django.utils.translation import gettext_lazy as _


class ArticleForm(forms.ModelForm):
    """
    Creates a form the staff can fill out on the site to
    post articles.
    """
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
            'content': SummernoteWidget(),
        }
        labels = {
            'content': 'Content*',
        }
        fields = ['title', 'content', 'excerpt', 'tags']


class CommentForm(forms.ModelForm):
    """
    Creates a form logged in users can fill out underneath
    articles that will be sent to the database to be approved.
    """
    subject = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,
                              'cols': 80}))

    class Meta:
        model = Comment
        fields = ['subject', 'content']
