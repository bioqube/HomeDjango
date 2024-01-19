from django.shortcuts import render

def auth(request):
    context = {
        'title' : 'Авторизация пользователя'
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Регистрация пользователя'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Личный кабинет'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    pass