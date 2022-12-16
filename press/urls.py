from django.urls import path
from . import views

urlpatterns = [
    path('', views.PressList.as_view(), name='home'),
    path('post-article', views.post_article, name='post-article'),
    path('edit-article/<slug:slug>', views.edit_article, name='edit-article'),
    path('delete/<slug:slug>', views.delete_article, name='delete'),
    path('fave-article/<slug:slug>', views.favorite_article, name='favorite'),
    path('<slug:slug>/', views.ArticleDetail.as_view(),
         name='article-detail'),
]