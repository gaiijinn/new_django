from django.shortcuts import render, HttpResponse
from products.models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        "title": 'Главная',
        "is_promotion": True,
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        "title": "Каталог",
        "products": Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)

