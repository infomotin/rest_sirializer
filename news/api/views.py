from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import Article
from news.api.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


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


# Class based views as a inherited with APIViews
class ArticleListViewsCreateViews(APIView):
    def get(self, request):
        article = Article.objects.filter(active=True)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
