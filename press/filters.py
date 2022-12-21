import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    tags = django_filets.CharFilter(lookup_expr='icontains')
    favorites = django_filets.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article 
        fields = ['favorites', 'tags']

    @property
    def qs(self):
        parent = super().qs
        favorites = getattr(self.request, 'user', None)
        return parent.filter(favorites=favorites)