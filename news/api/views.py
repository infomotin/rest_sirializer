from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Article
from news.api.serializers import ArticleSerializer


# this is Functions Based View
@api_view(["GET", "POST"])
def listCreateArticleSerializer(request):
    if request.method == "GET":
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_detais_views(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        # status = status.Http_404_NOT_FOUND
        Error = {
            "Error": {
                "code": 404,
                "message": "Article Not Found"
            },
            "status": {
                "status": 'Http_404_NOT_FOUND'
            }
        }
        return Response(Error, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
