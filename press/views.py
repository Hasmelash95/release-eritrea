from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(queryset, slug=slug)
        comment = article.comment.filter(approved=True).order_by('created_on')

def home_page(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')
