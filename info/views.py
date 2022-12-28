from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import generic, View


def say_hello(request):
    return HttpResponse("Hello!")
