from django.urls import path
from . import views

# Url patterns for info app

urlpatterns = [
    path('', views.Info.as_view(), name='info'),
]

