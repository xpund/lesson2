from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest



def auth(request):
    return render(request, 'users/users.html')


def reg(request):
    a = request.META.get('REMOTE_ADDR')
    return HttpResponse("Регистрация для, " + str(a))


def recover_pass(request):
    a = request.META.get('REMOTE_ADDR')
    return HttpResponse("Восстановить пароль для, " + str(a))
