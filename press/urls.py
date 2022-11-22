from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('', views.ArticleList.as_view(), name='press'),
]