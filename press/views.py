from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Article, Picture
from .forms import CommentForm, ArticleForm
from .filters import ArticleFilter
from django.template.defaultfilters import slugify
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required                                               
from django.contrib import messages


class PressList(generic.ListView):
    model = Article
    queryset = Article.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(PressList, self).get_context_data(**kwargs)
        context['picture'] = Picture.objects.all()
        return context


@staff_member_required
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


@staff_member_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_form = ArticleForm(request.POST or None, instance=article)
    if article_form.is_valid():
        article_form.save()
        return redirect('/' + slug)
    return render(request, 'edit-article.html', {'article_form': article_form})


@staff_member_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.POST:
        article.delete()
        HttpResponseRedirect('/')
    return render(request, 'delete.html', {'article': article})


@login_required
def favorite_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if article.favorites.filter(id=request.user.id).exists():
        is_fave = True
    else:
        is_fave = False
    if request.POST:
        if article.favorites.filter(id=request.user.id).exists():
            article.favorites.remove(request.user)
            return redirect('/' + slug)
        else:
            article.favorites.add(request.user)
            return redirect('/' + slug)
    return render(request, 'fave-add.html', {'article': article, 'is_fave': is_fave})


def article_filter(request):
    f = ArticleFilter(request.GET, queryset=Article.objects.all())
    return render(request, 'article-filter.html', {'filter': f})


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
                                                         'created_on')
        return render(
            request,
            'article-detail.html',
            {
                'article': article,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
                                                         'created_on')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'article-detail.html',
            {
                'article': article,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm()
            }
        )
