from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    # model юзера указана в settings
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Вход'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'Регистрация'
    model = User
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')  # вместо обычного reverse
    success_message = 'Поздравляем! Вы успешно создали аккаунт.'


class UserProfileView(TitleMixin, UpdateView):
    title = 'Профиль'
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm

    def get_success_url(self):  # вместо reverse_lazy потому что в у нас в url появился id
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Верификация'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = self.kwargs.get('code')
        user = User.objects.get(email=self.kwargs['email'])
        email_verif = EmailVerification.objects.filter(user=user, code=code)

        if email_verif.exists() and not email_verif.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))