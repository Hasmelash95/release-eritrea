from django.urls import path
from . import views

urlpatterns = [
    path('', views.Info.as_view(), name='info'),
]

