from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


def home_page(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

