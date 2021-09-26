from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')[:5]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create_task(request):
    return render(request, 'main/create.html')