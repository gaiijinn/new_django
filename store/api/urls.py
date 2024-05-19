from django.urls import path
from api.views import ProductsListView, ProductByCategoryListView, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

app_name = "api"

urlpatterns = [
    path('get-products/', ProductsListView.as_view(), name='get_products'),
    path('get-products/<int:category_id>/', ProductByCategoryListView.as_view(), name='get_products_by_id'),

]

urlpatterns += router.urls