from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comment(models.Model):
    class Meta():
        db_table = 'comments'
    comment_text = models.TextField()
    comment_article = models.ForeignKey(Article)
    comment_date = models.DateTimeField()
    comment_from = models.ForeignKey(User)
