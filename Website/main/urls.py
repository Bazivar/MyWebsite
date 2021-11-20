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
    path('articles/article_integration', views.article, {'article_number': 'integration'}, name = 'article_integration'),
    path('articles/article_vulnerabilities', views.article, {'article_number': 'vulnerabilities'}, name = 'article_vulnerabilities'),
    path('articles/article_time', views.article, {'article_number': 'time'}, name = 'article_time'),
    path('articles/article_solar', views.article, {'article_number': 'solar'}, name = 'article_solar'),

    #courses

    #kb_articles
    path('knowledge_base/cmos', views.kb_article, {'kb_article_number' : 'cmos'}, name = 'cmos'),
    path('knowledge_base/analog_video', views.kb_article, {'kb_article_number' : 'analog_video'}, name = 'analog_video'),
    path('knowledge_base/ip_video', views.kb_article, {'kb_article_number' : 'ip_video'}, name = 'ip_video'),
    path('knowledge_base/structure_cabling', views.kb_article, {'kb_article_number' : 'structure_cabling'}, name = 'structure_cabling'),
    path('knowledge_base/cable_trays', views.kb_article, {'kb_article_number' : 'cable_trays'}, name = 'cable_trays'),
    path('knowledge_base/ups_system', views.kb_article, {'kb_article_number' : 'ups_system'}, name = 'ups_system'),
    path('knowledge_base/disk_system', views.kb_article, {'kb_article_number' : 'disk_system'}, name = 'disk_system'),
]