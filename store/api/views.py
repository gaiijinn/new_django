from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from products.models import Product, ProductCategory
from api.serializers import ProductSerializers, CategorySerializer
from django.shortcuts import get_object_or_404
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class ProductsListView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers


class ProductByCategoryListView(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(ProductCategory, id=category_id)
        return Product.objects.filter(category=category).order_by('-id')

