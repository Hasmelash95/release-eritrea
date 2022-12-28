from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    image = CloudinaryField('image', default='temporary')
    job_title = models.CharField(max_length=30, default='Volunteer')
    about = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.first_name + self.last_name


class Location(models.Model):
    name = models.CharField(max_length=60)
    street_name = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

