from django.urls import path, include
from news.api.views import listCreateArticleSerializer, article_detais_views

urlpatterns = [
    path("api-list/", listCreateArticleSerializer, name='apilist'),
    path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),
    #path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),
]
