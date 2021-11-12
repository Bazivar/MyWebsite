from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('articles', views.articles, name = 'articles'),
    path('courses', views.courses, name = 'courses'),
    path('knowledge_base', views.knowledge_base, name = 'knowledge_base'),
    path('projects', views.projects, name = 'projects'),
    path('social_networks', views.social_networks, name = 'social_networks'),
    path('about', views.about, name = 'about'),

    #articles
    path('articles/article_integration', views.article_integration, name = 'article_integration'),
    path('articles/article_vulnerabilities', views.article_vulnerabilities, name = 'article_vulnerabilities'),
    path('articles/article_time', views.article_time, name = 'article_time'),
    path('articles/article_solar', views.article_solar, name = 'article_solar'),

    #courses

    #kb_articles
    path('knowledge_base/cmos', views.kb_cmos, name = 'cmos'),
]