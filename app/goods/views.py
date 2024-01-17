from django.shortcuts import render
from goods.models import Category, Product


def catalog(request, cat_slug):

    if cat_slug=='all':
        goods = Product.objects.all()
    else:
        goods = Product.objects.filter(category__slug=cat_slug)

    context = {
        'title' : 'Каталог товаров',
        'goods' : goods,

        }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product' : product,
    }

    return render(request, 'goods/product.html', context)
