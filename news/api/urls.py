from django.urls import path, include
from news.api.views import listCreateArticleSerializer

urlpatterns = [
    path("api-list/", listCreateArticleSerializer, name='apilist'),
]
