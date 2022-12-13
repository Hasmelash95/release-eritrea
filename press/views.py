from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Article
from .forms import CommentForm, ArticleForm
from django.template.defaultfilters import slugify


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def post_article(request):
    if request.POST:
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = request.user
            new_article.slug = slugify(new_article.title)
            new_article.save()
            return redirect('/')
    return render(request, 'post-article.html', {'article_form': ArticleForm})



def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_form = ArticleForm(request.POST or None, instance=article)
    if article_form.is_valid():
        article_form.save()
        return redirect('/' + slug)
    return render(request, 'edit-article.html', {'article_form': article_form})


def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.POST:
        article.delete()
        return redirect('/')
    return render(request, 'delete.html', {'article': article})


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
                "commented": False,
                "comment_form": CommentForm()     
            }
        )

    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm(data=request.POST)  
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article-detail.html",
            {
                "article": article,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()     
            }
        )  
