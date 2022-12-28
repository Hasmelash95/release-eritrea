from django.contrib import admin
from .models import Profile, Location


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'street_name', 'city')
