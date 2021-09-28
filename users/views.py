from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterUserForm

from django.contrib.auth.decorators import login_required

def userLoginName(request):
    if request.user.is_authenticated:
        return username


def auth(request):
    if request.user.is_authenticated:
        return redirect('users:lk')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:lk')
        else:
            messages.info(request, "Нет такой связки пользователь/пароль")

    context = {}
    return render(request, 'users/users.html', context)


def logoutUser(request):
    logout(request)
    return redirect('main:index')


def reg(request):
    if request.user.is_authenticated:
        return redirect('users:lk')

    form = RegisterUserForm
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Пользователь ' + str(user) + ' успешно зарегистрирован/nВы можете войти в систему!')
            return redirect('users:auth')

    context = {'form': form}
    return render(request, 'users/reg.html', context)


def recover_pass(request):
    context = {}
    return render(request, 'users/recover_pass.html', context)


@login_required(login_url='users:auth')
def lkUser(request):
    context = {}
    return render(request, 'lk_head.html', context)
