from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET"])
def listCreateArticleSerializer(request):
    if request.method == "GET":
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article,many=True)
        return Response(serializer.data)

