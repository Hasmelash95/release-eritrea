from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('detail/<slug:slug>', views.ArticleDetail.as_view(), 
         name='article_detail'),
    path('create/', views.ArticlePost.as_view(), name='create'),

]