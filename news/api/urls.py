from django.urls import path, include
from news.api.views import (listCreateArticleSerializer,
                            article_detais_views,
                            ArticleListViewsCreateViews,
                            ArticleDetailView)

urlpatterns = [
    path("api-list/", listCreateArticleSerializer, name='apilist'),
    path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),
    path("class-api", ArticleListViewsCreateViews.as_view(), name='class-apilist'),
    path("class-api/<int:pk>/", ArticleDetailView.as_view(), name='class-apicrud'),
    #path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),
]
