from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'approved')
    summernote_fields = ('content')


