from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article
from .forms import CommentForm, ArticleForm


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class PostArticle(View):

    def post(self, request):
        if request.user.is_staff:
            article_form = ArticleForm(data=request.POST)
            if form.is_valid():
                article_form.instance.author = request.user.username
                article = article_form.save(commit=False)
                messages.success(request, 'has been successfully posted')
                article.save
            else:
                messages.fail(request, 'is not valid')
                article_form = ArticleForm()
            return render(
                request, 'index.html',
                {'article_form': ArticleForm()}
            )    

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
