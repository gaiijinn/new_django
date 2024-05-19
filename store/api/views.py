from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from products.models import Product, ProductCategory
from api.serializers import ProductSerializers, CategorySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

    def get_permissions(self):
        if self.action in ('post', 'destroy', 'patch'):
            self.permission_classes = (IsAdminUser, )
        else:
            self.permission_classes = (IsAuthenticated, )

        return super(CategoryViewSet, self).get_permissions()


class ProductsListView(ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers


class ProductByCategoryListView(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(ProductCategory, id=category_id)
        return Product.objects.filter(category=category).order_by('-id')

