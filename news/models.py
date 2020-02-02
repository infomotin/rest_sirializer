from django.db import models


# from news.api.serializers import ArticleSerializer

class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Create your models here.
class Article(models.Model):
    # author = models.CharField(max_length=50)
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=120)
    descriptions = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=200)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"
