from django.http import Http404
from django.shortcuts import render
from .models import Article, Comment


def blog(request):
    articles = Article.objects.order_by('-id')[:5]
    context = {'article': articles}
    return render(request, 'blog.html', context)


def article(request, article_id):
    try:
        ar = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    context = {'title': ar.title, 'art': ar}
    return render(request, 'blog/art.html', context)
