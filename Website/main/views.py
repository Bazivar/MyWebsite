from django.shortcuts import render
import os
from .list_of_articles import all_articles
from .list_of_articles_en import all_articles_en
from .list_of_kb_articles import all_kb_articles
from .list_of_kb_articles_en import all_kb_articles_en

######################## Main page.#####################################
def home(request):
    data = {
        'title': 'Василий Перевощиков - Главная сайта',
        'h1': 'Василий Перевощиков - инженер систем безопасности',
        }
    return render(request, 'main/home.html', data)

def home_en(request):
    data = {
        'title': 'Vasil Peravoshchykau - Main page',
        'h1': 'Vasil Peravoshchykau - security systems engineer',
        }
    return render(request, 'main/home_en.html', data)

######################## Articles, blog .#####################################
def articles(request):
    list_of_articles = all_articles.values()
    data = {
        'title': 'Сайт Василия Перевощикова - Статьи',
        'h1': 'Статьи Василия Перевощикова',
        'all_articles': list_of_articles,
    }
    return render(request, 'main/articles.html', data)

def articles_en(request):
    list_of_articles = all_articles_en.values()
    data = {
        'title': "Vasily Perevoshchikov's website - Articles",
        'h1': 'Articles by Vasily Perevoshchikov',
        'all_articles': list_of_articles,
    }
    return render(request, 'main/articles_en.html', data)

######################## Courses .#####################################
def courses(request):
    data = {
        'title': 'Курсы Василия Перевощикова',
        'h1': 'Курсы по системам безопасности от Василия Перевощикова',
        # 'all_courses': all_courses,
    }
    return render(request, 'main/courses.html', data)

def courses_en(request):
    data = {
        'title': 'Courses by Vasily Perevoshchikov',
        'h1': 'Courses on security systems from Vasily Perevoshchikov',
        # 'all_courses': all_courses,
    }
    return render(request, 'main/courses_en.html', data)

######################## Knowledge_base #####################################
def knowledge_base(request):
    kb_articles = all_kb_articles.values()
    data = {
        'title': 'База знаний Василия Перевощикова',
        'h1': 'База знаний и фактов о системах безопасности',
        'all_kb_articles': kb_articles,
    }
    return render(request, 'main/knowledge_base.html', data)

def knowledge_base_en(request):
    kb_articles = all_kb_articles_en.values()
    data = {
        'title': 'Vasily Perevoshchikov Knowledge Base',
        'h1': 'Knowledge base and facts about security systems',
        'all_kb_articles': kb_articles,
    }
    return render(request, 'main/knowledge_base_en.html', data)

######################## Projects #####################################
def projects(request):
    data = {
        'title': 'Проекты Василия Перевощикова',
        'h1': 'Разработанные мной проекты',
    }
    return render(request, 'main/projects.html', data)

def projects_en(request):
    data = {
        'title': 'Projects by Vasily Perevoshchikov',
        'h1': "My projects that I've developed through my career",
    }
    return render(request, 'main/projects_en.html', data)

######################## Social networks #####################################
def social_networks(request):
    data = {
        'title': 'Социальные сети Василия Перевощикова',
        'h1': 'Где можно меня найти',
    }
    return render(request, 'main/social_networks.html', data)

def social_networks_en(request):
    data = {
        'title': 'Social networks of Vasily Perevoshchikov',
        'h1': 'Where can you find me',
    }
    return render(request, 'main/social_networks_en.html', data)

######################## About #####################################
def about(request):
    data = {
        'title': 'Василий Перевощиков: обо мне',
        'h1': 'Сам про себя: кто такой и что умею',
    }
    return render(request, 'main/about.html', data)

def about_en(request):
    data = {
        'title': 'Vasyly Perevoshchikov: About me',
        'h1': 'About myself: who I am and what can I do',
    }
    return render(request, 'main/about_en.html', data)

######################## Articles.#####################################
def article (request, article_number):
    src = os.path.dirname(os.path.realpath(__file__)) + all_articles[article_number]['html_page']

    data = {
        'title': all_articles[article_number]['page_title'],
        'h1': all_articles[article_number]['article_title'],
        'description': all_articles[article_number]['description'],
        'keywords': all_articles[article_number]['keywords'],
        'article_image': all_articles[article_number]['image'],
        'original': all_articles[article_number]['original'],
        'source': all_articles[article_number]['source'],
        'date': all_articles[article_number]['date'],
        'src': src,
    }
    return render(request, 'main/single_article.html', data)


def article_en (request, article_number):
    src = os.path.dirname(os.path.realpath(__file__)) + all_articles_en[article_number]['html_page']

    data = {
        'title': all_articles_en[article_number]['page_title'],
        'h1': all_articles_en[article_number]['article_title'],
        'description': all_articles_en[article_number]['description'],
        'keywords': all_articles_en[article_number]['keywords'],
        'article_image': all_articles_en[article_number]['image'],
        'original': all_articles_en[article_number]['original'],
        'source': all_articles_en[article_number]['source'],
        'date': all_articles_en[article_number]['date'],
        'src': src,
    }
    return render(request, 'main/single_article_en.html', data)


######################## Knowledge_base.#####################################
def kb_article (request, kb_article_number):

    src = os.path.dirname(os.path.realpath(__file__)) + all_kb_articles[kb_article_number]['html_page']
    data = {
        'title': all_kb_articles[kb_article_number]['page_title'],
        'h1': all_kb_articles[kb_article_number]['article_title'],
        'description': all_kb_articles[kb_article_number]['description'],
        'keywords': all_kb_articles[kb_article_number]['keywords'],
        'article_image': all_kb_articles[kb_article_number]['image'],
        'src': src,
    }
    return render(request, 'main/kb_article.html', data)

def kb_article_en (request, kb_article_number):

    src = os.path.dirname(os.path.realpath(__file__)) + all_kb_articles_en[kb_article_number]['html_page']
    data = {
        'title': all_kb_articles_en[kb_article_number]['page_title'],
        'h1': all_kb_articles_en[kb_article_number]['article_title'],
        'description': all_kb_articles_en[kb_article_number]['description'],
        'keywords': all_kb_articles_en[kb_article_number]['keywords'],
        'article_image': all_kb_articles_en[kb_article_number]['image'],
        'src': src,
    }
    return render(request, 'main/kb_article_en.html', data)