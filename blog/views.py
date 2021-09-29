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

    lastest_comment_list = ar.comment_set.order_by("-id")[:10]

    context = {'title': ar.title, 'art': ar, 'last_comment': lastest_comment_list}
    return render(request, 'blog/art.html', context)
