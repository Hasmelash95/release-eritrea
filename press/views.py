from django.shortcuts import render, HttpResponse
from django.template import loader
from django.views import generic
from .models import Article


def home_page(request):
    first_template = loader.get_template('index.html')
    return HttpResponse(first_template.render())


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3