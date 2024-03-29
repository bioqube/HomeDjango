from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegForm

def login(request):
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()


    context = {
        'title' : 'Авторизация пользователя',
        'form' : form,
    }

    return render(request, 'users/login.html', context)


def registration(request):

    if request.method =='POST':
        form = UserRegForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegForm()

    context = {
        'title': 'Регистрация пользователя',
        'form' : form,
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Личный кабинет'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))