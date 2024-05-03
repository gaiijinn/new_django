import os
from http import HTTPStatus

import django
from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory

# для того чтобы community версия могла в дебаг режиме запускать тесты
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path=path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Магазин')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCASE(TestCase):
    fixtures = ['cats.json', 'prod.json']

    def setUp(self):
        self.product = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path=path)

        self._common_test(response=response)
        self.assertEqual(list(response.context_data['object_list']), list(self.product[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path=path)

        self._common_test(response=response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.product.filter(category_id=category.id))
        )

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
