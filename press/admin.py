from django.contrib import admin
from .models import Article, Comment, Picture
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('tags', 'favorites', 'author')
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on', 'approved', 'updated_on')
    list_filter = ('user', 'approved')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
