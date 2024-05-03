from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm
from users.models import EmailVerification, User

# Create your tests here.


class UserRegistrationTestView(TestCase):
    def setUp(self) -> None:
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Влад',
            'last_name': 'Рубан',
            'username': 'gaijin',
            'email': 'vladruban8@gmail.com',
            'password1': 'Vlad8900656',
            'password2': 'Vlad8900656',
        }

    def test_reg_view_get(self):
        response = self.client.get(path=self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_reg_view_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username=username).exists())

        # email
        email = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email.exists())

    def test_reg_view_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
