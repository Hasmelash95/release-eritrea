from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article
from .forms import CommentForm


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        return render(
            request,
            "article-detail.html",
            {
                "article": article,
                "comments": comments,
                "comment_form": CommentForm()     
            }
        )

def home_page(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')
