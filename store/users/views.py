from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid(): #если правильно ввел
            username = request.POST['username'] #достаем данные которые получили
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password) #проверяем юзера

            if user: #если такой юзер есть логинимся
                print("login succes")
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:                         #когда чел заходит на логин
        form = UserLoginForm()

    context = {'form': form}

    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно создали акаунт.')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print("reg_user_error")

    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'users/registration.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "title": "Профиль",
        'form': form,
        'baskets': Basket.objects.filter(user=request.user).all() #только корзину юзера
    }

    return render(request, 'users/profile.html', context=context)


def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('products:index'))