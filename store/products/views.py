from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin  # наш миксин
from products.models import Basket, Product, ProductCategory

# Create your views here.


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Магазин'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['is_promotion'] = False

        return context


class ProductsListVies(TitleMixin, ListView):
    model = Product  # модель из бд
    template_name = "products/products.html"
    paginate_by = 3  # для пагинатора + изменился код в шаблонеs
    title = 'Каталог'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListVies, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()

        return context

    def get_queryset(self):
        queryset = super(ProductsListVies, self).get_queryset()  # типо как all для нашей модели
        # print(self.kwargs) #в этот словарь получаем значения
        category_id = self.kwargs.get('category_id')  # из юрлг где указываем что передаем
        return queryset.filter(category=category_id) if category_id else queryset


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)  # получаем продукт по id НЕ ВСЕ СРАЗУ
    baskets = Basket.objects.filter(user=request.user, product=product)  # смотрим есть ли такой продукт в кверисете

    if not baskets.exists():  # если квери сет пустой
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # создаем в бд запись продукта и количества, как в моделе
    else:  # если по КОНКРЕТНОМУ продукту квери сет НЕ ПУСТОЙ
        basket = baskets.first()  # берем значение
        basket.quantity += 1  # добавляем количество его
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # возращаем на ту страницу где находиться чел


@login_required
def basket_remove(request, basket_id):  # у нас по сути много корзинок*
    basket = Basket.objects.get(id=basket_id)  # берем нужную и удаляем
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
