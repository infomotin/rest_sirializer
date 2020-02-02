from django.urls import path, include
from news.models import *
from news.api.views import (listCreateArticleSerializer,
                            article_detais_views,
                            ArticleListViewsCreateViews,
                            ArticleDetailView,
                            JournalistSerializerApiViews,
                            JournalistDetailView)

urlpatterns = [

    # functions Based Views
    path("api-list/", listCreateArticleSerializer, name='apilist'),
    path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),

    # class Based Views
    path("class-api", ArticleListViewsCreateViews.as_view(), name='class-apilist'),
    path("class-api/<int:pk>/", ArticleDetailView.as_view(), name='class-apicrud'),

    # class Base JournalistDetailView Viewa
    path("class-jou/", JournalistSerializerApiViews.as_view(), name='class-apijur'),
    path("class-jou/<int:pk>/", JournalistDetailView.as_view(), name='class-apicurd'),
    # path("api-crud/<int:pk>/", article_detais_views, name='apicrud'),
]
