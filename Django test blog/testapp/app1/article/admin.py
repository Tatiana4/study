from django.contrib import admin
from article.models import Article, Comment

# Register your models here.

class ArticleInline(admin.StackedInline): #для работы с комментами
    model = Comment
    extra = 2 #сколько полей для комментов надо отображать

class ArticleAdmin(admin.ModelAdmin): #здесь указываем поля, видимые в админке
    fields = ['article_title', 'article_text', 'article_data']
    inlines = [ArticleInline] #поля для комментариев будут отображаться при работе со статьями
    list_filter = ['article_data'] #в админке появится возможность фильтрации по введенному здесь значению

admin.site.register(Article, ArticleAdmin)
