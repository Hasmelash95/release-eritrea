from django.urls import path
from info.views import say_hello

urlpatterns = [
    path('', say_hello, name='info'),
]

