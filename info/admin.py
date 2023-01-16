from django.contrib import admin
from .models import Profile, Location


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    The view on the admin site for the Profile model
    """
    list_display = ('first_name', 'last_name', 'job_title', 'created_on')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    The view on the admin site for the Location model
    """
    list_display = ('name', 'street_name', 'city', 'created_on')
