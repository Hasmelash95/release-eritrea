from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    article_form = ArticleForm()
    if request.POST:
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            new_article = article_form.save(commit=False)
            new_article.author = request.user
            new_article.slug = slugify(new_article.title)
            new_article.save()
            messages.success(request, 'Article successfully posted.')
            return redirect(reverse('article-detail', args=[new_article.slug]))
        elif article_form.errors:
            messages.error(request,
                           'There was a problem submitting the form.'
                           ' Make sure all required fields are filled.')
    return render(request, 'post-article.html', {'article_form': article_form})


@staff_member_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article_form = ArticleForm(request.POST or None, instance=article)
    if article_form.is_valid():
        article = article_form.save(commit=False)
        article.slug = slugify(article.title)
        article_form.save()
        messages.success(request, 'Article successfully updated.')
        return redirect(reverse('article-detail', args=[article.slug]))
    elif article_form.errors:
        messages.error(request,
                       'There was a problem submitting the form.'
                       ' Make sure all required fields are filled.')
    return render(request, 'edit-article.html', {'article_form': article_form})


@staff_member_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.POST:
        article.delete()
        messages.success(request, 'Article deleted.')
        return redirect('/#press')
    return render(request, 'delete.html', {'article': article})


@login_required
def favorite_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    is_fave = False
    if article.favorites.filter(id=request.user.id).exists():
        is_fave = True
    if request.POST:
        if article.favorites.filter(id=request.user.id).exists():
            article.favorites.remove(request.user)
            messages.success(request, 'Article removed from favorites.')
            return redirect(reverse('article-detail', args=[slug]))
        else:
            article.favorites.add(request.user)
            messages.success(request, 'Article added to favorites.')
            return redirect(reverse('article-detail', args=[slug]))
    return render(
        request,
        'fave-add.html',
        {
            'article': article,
            'is_fave': is_fave,
        }
        )


def article_filter(request):
    f = ArticleFilter(request.GET, queryset=Article.objects.all())
    return render(request, 'article-filter.html', {'filter': f})


@login_required
def favorites(request):
    articles = request.user.favorite.all()
    return render(request, 'favorites.html', {'articles': articles})


class ArticleDetail(View):

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
                                                         'created_on')
        is_fave = False
        if article.favorites.filter(id=request.user.id).exists():
            is_fave = True
        return render(
            request,
            'article-detail.html',
            {
                'article': article,
                'comments': comments,
                'commented': False,
                'is_fave': is_fave,
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
            messages.success(request, 'Your comment is awaiting approval.')
            comment.save()
        elif comment_form.errors:
            messages.error(request, 'There was a problem submitting the form.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            'article-detail.html',
            {
                'article': article,
                'comments': comments,
                'comment_form': CommentForm()
            }
        )
