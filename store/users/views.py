from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin

from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


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
    success_url = reverse_lazy('users:login') #вместо обычного reverse
    success_message = 'Поздравляем! Вы успешно создали аккаунт.'


class UserProfileView(TitleMixin, UpdateView):
    title = 'Профиль'
    model = User
    template_name = "users/profile.html"
    form_class = UserProfileForm

    def get_success_url(self): #вместо reverse_lazy потому что в у нас в url появился id
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


# def logout(request):
#     auth.logout(request)
#
#     return HttpResponseRedirect(reverse('products:index'))

# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid(): #если правильно ввел
#             username = request.POST['username'] #достаем данные которые получили
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password) #проверяем юзера
#             if user: #если такой юзер есть логинимся
#                 print("login succes")
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:                         #когда чел заходит на логин
#         form = UserLoginForm()
#
#     context = {'form': form}
#     return render(request, 'users/login.html', context=context)


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно создали акаунт.')
#             return HttpResponseRedirect(reverse('users:login'))
#         else:
#             print("reg_user_error")
#     else:
#         form = UserRegistrationForm()
#
#     context = {'form': form}
#     return render(request, 'users/registration.html', context=context)


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {
#         "title": "Профиль",
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user).all() #только корзину юзера
#     }
#     return render(request, 'users/profile.html', context=context)