from django.shortcuts import render, redirect
from .models import Article
import time

# Create your views here.
def index_defined_in_view(request):
    movie_articles_num = Article.objects.filter(category="movie").count()
    entertain_articles_num = Article.objects.filter(category="entertain").count()
    drama_articles_num = Article.objects.filter(category="drama").count()

    return render(request, 'index_in_templates.html', {'movie_articles_num': movie_articles_num, 'entertain_articles_num': entertain_articles_num, 'drama_articles_num':  drama_articles_num})

def detail_defined_in_view(request, primary_key_of_the_article_i_clicked):
    article = Article.objects.get(pk=primary_key_of_the_article_i_clicked)
    return render(request, 'detail_in_templates.html', {'an_article_i_will_use_in_html': article})

def new_defined_in_view(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = time.strftime('%c', time.localtime(time.time()))
        )
        return redirect('detail_i_will_use_in_html', primary_key_of_the_article_i_clicked=new_article.pk)
    else:
        return render(request, 'new_in_templates.html')

def movies_in_view(request):
    movie_article_title = Article.objects.filter(category="movie")
    return render(request, 'movie_in_templates.html', {'movie_article_title': movie_article_title})

def entertain_in_view(request):
    entertain_article_title = Article.objects.filter(category="entertain")
    return render(request, 'entertain_in_templates.html', {'entertain_article_title': entertain_article_title})

def drama_in_view(request):
    drama_article_title = Article.objects.filter(category="drama")
    return render(request, 'drama_in_templates.html', {'drama_article_title': drama_article_title})