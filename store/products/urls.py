from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ProductsListVies, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path('',ProductsListVies.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListVies.as_view(), name='category'),
    # ../products/category/<product_category_id>/..
    path('page/category/<int:page>/', ProductsListVies.as_view(), name='paginator'),
    # page для view, html для пагинатора
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
