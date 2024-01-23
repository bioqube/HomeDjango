from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from goods.models import Product


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    #return Product.objects.filter(description__search=query)

    return Product.objects.annotate(search=SearchVector("name", "description")).filter(search=query)
