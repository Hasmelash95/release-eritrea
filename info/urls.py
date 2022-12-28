from django.urls import path
from info.views import info_profile

urlpatterns = [
    path('', info_profile , name='info'),
]

