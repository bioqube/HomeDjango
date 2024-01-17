from django.shortcuts import render
from goods.models import Category, Product


def catalog(request):

    goods = Product.objects.all()

    context = {
        'title' : 'Каталог товаров',
        'goods' : goods,

        }
    return render(request, 'goods/catalog.html', context)

def product(request, product_id):

    product = Product.objects.get(id=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'goods/product.html', context)
