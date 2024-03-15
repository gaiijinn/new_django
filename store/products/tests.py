from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

import os
import django

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
