from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE,
                               related_name='press_releases')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite',
                                       default=None, blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,
                             related_name='commenter')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    subject = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.user


class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    alt = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=None, height_field=None,
                              width_field=None, max_length=500)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
