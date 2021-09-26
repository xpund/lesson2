from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from users.forms import RegisterUserForm


def auth(request):
    context = {}
    return render(request, 'users/users.html', context)


def reg(request):
    form = RegisterUserForm
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:auth')

    context = {'form': form}
    return render(request, 'users/reg.html', context)


def recover_pass(request):
    context = {}
    return render(request, 'users/recover_pass.html', context)
