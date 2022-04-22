from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('en/', views.home_en, name = 'home_en'),
    path('articles', views.articles, name = 'articles'),
    path('en/articles', views.articles_en, name = 'articles_en'),
    path('courses', views.courses, name = 'courses'),
    path('en/courses', views.courses_en, name = 'courses_en'),
    path('knowledge_base', views.knowledge_base, name = 'knowledge_base'),
    path('en/knowledge_base', views.knowledge_base_en, name = 'knowledge_base_en'),
    path('projects', views.projects, name = 'projects'),
    path('en/projects', views.projects_en, name = 'projects_en'),
    path('social_networks', views.social_networks, name = 'social_networks'),
    path('en/social_networks', views.social_networks_en, name = 'social_networks_en'),
    path('about', views.about, name = 'about'),
    path('en/about', views.about_en, name = 'about_en'),

    #articles
    path('articles/article_integration', views.article, {'article_number': 'integration'}, name = 'article_integration'),
    path('en/articles/article_integration', views.article_en, {'article_number': 'integration'}, name = 'article_integration_en'),
    path('articles/article_vulnerabilities', views.article, {'article_number': 'vulnerabilities'}, name = 'article_vulnerabilities'),
    path('en/articles/article_vulnerabilities', views.article_en, {'article_number': 'vulnerabilities'}, name = 'article_vulnerabilities_en'),
    path('articles/article_time', views.article, {'article_number': 'time'}, name = 'article_time'),
    path('en/articles/article_time', views.article_en, {'article_number': 'time'}, name = 'article_time_en'),
    path('articles/article_solar', views.article, {'article_number': 'solar'}, name = 'article_solar'),
    path('en/articles/article_solar', views.article_en, {'article_number': 'solar'}, name = 'article_solar_en'),

    #courses

    #kb_articles
    path('knowledge_base/cmos', views.kb_article, {'kb_article_number' : 'cmos'}, name = 'cmos'),
    path('en/knowledge_base/cmos', views.kb_article_en, {'kb_article_number' : 'cmos'}, name = 'cmos_en'),
    path('knowledge_base/analog_video', views.kb_article, {'kb_article_number' : 'analog_video'}, name = 'analog_video'),
    path('en/knowledge_base/analog_video', views.kb_article_en, {'kb_article_number' : 'analog_video'}, name = 'analog_video_en'),
    path('knowledge_base/ip_video', views.kb_article, {'kb_article_number' : 'ip_video'}, name = 'ip_video'),
    path('en/knowledge_base/ip_video', views.kb_article_en, {'kb_article_number' : 'ip_video'}, name = 'ip_video_en'),
    path('knowledge_base/structure_cabling', views.kb_article, {'kb_article_number' : 'structure_cabling'}, name = 'structure_cabling'),
    path('en/knowledge_base/structure_cabling', views.kb_article_en, {'kb_article_number' : 'structure_cabling'}, name = 'structure_cabling_en'),
    path('knowledge_base/cable_trays', views.kb_article, {'kb_article_number' : 'cable_trays'}, name = 'cable_trays'),
    path('en/knowledge_base/cable_trays', views.kb_article_en, {'kb_article_number' : 'cable_trays'}, name = 'cable_trays_en'),
    path('knowledge_base/ups_system', views.kb_article, {'kb_article_number' : 'ups_system'}, name = 'ups_system'),
    path('en/knowledge_base/ups_system', views.kb_article_en, {'kb_article_number' : 'ups_system'}, name = 'ups_system_en'),
    path('knowledge_base/disk_system', views.kb_article, {'kb_article_number' : 'disk_system'}, name = 'disk_system'),
    path('en/knowledge_base/disk_system', views.kb_article_en, {'kb_article_number' : 'disk_system'}, name = 'disk_system_en'),
]