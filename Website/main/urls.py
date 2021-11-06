from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('articles', views.articles, name = 'articles'),
    path('articles/article_integration', views.article_integration, name = 'article_integration'),
    path('articles/article_vulner', views.article_vulner, name = 'article_vulner'),
]