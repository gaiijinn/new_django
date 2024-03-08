from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket
from django.core.paginator import Paginator
from users.models import User

# Create your views here.


def index(request):
    context = {
        "title": 'Главная',
        "is_promotion": True,
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page) #пагинация
    products_paginator = paginator.page(page_number)

    context = {
        "title": "Каталог",
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }

    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id) #получаем продукт по id НЕ ВСЕ СРАЗУ
    baskets = Basket.objects.filter(user=request.user, product=product) #смотрим есть ли такой продукт в кверисете

    if not baskets.exists(): #если квери сет пустой
        Basket.objects.create(user=request.user, product=product, quantity=1) #создаем в бд запись продукта и количества, как в моделе
    else: #если по КОНКРЕТНОМУ продукту квери сет НЕ ПУСТОЙ
        basket = baskets.first() #берем значение
        basket.quantity += 1 #добавляем количество его
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER']) #возращаем на ту страницу где находиться чел


@login_required
def basket_remove(request, basket_id): #у нас по сути много корзинок*
    basket = Basket.objects.get(id=basket_id) #берем нужную и удаляем
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

