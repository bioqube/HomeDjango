from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Category


def index(request):

    context = {

        'title' : 'Главная страница',
        'content' : 'Магазин мебели HOME',

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title' : 'О нас',
        'content' : 'Текст о том какой классный этот интернет магазин.',
    }
    return render(request, 'main/about.html', context)
