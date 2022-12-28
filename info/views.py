from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Profile, Location


class Info(generic.ListView):
    model = Profile
    template_name = 'info/info.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(Info, self).get_context_data(**kwargs)
        context['location'] = Location.objects.all()
        return context