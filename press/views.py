from django.shortcuts import render, HttpResponse
from django.template import loader


def home_page(request):
    first_template = loader.get_template('index.html')
    return HttpResponse(first_template.render())
