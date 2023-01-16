import django_filters
from .models import Article


class ArticleFilter(django_filters.FilterSet):
    """
    Filters articles by tags and words the title contains
    """
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['tags']
