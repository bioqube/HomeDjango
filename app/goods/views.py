from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Product


def catalog(request, cat_slug):

    page = request.GET.get('page', 1)

    if cat_slug=='all':
        goods = Product.objects.all()
    else:
        goods = Product.objects.filter(category__slug=cat_slug)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)


    context = {
        'title' : 'Каталог товаров',
        'goods' : current_page,
        'slug_url' : cat_slug,
        }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product' : product,
    }

    return render(request, 'goods/product.html', context)
