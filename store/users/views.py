from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
<<<<<<< HEAD
from django.urls import reverse

# Create your views here.
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == "POST": #проверка являеться ли запрос типа ПОСТ
        form = UserLoginForm(data=request.POST) #получаем данные которые были заполнены
        if form.is_valid(): #валидация
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) #аутентификация проверяем есть ли юзер в бд
            if user.last_name == 'Владислав':
                print('ok')

            if user:
                auth.login(request, user) #авторизация
                return HttpResponseRedirect(reverse('index')) #переадресация
        else:
            print(form.errors)

    else: #если гет
        form = UserLoginForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context)
=======
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
>>>>>>> after_pause


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
<<<<<<< HEAD
        if form.is_valid():
            form.save() #сохранит обьект в бд
            messages.success(request, 'Успешная реестрация')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
=======

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
>>>>>>> after_pause

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
<<<<<<< HEAD
    context = {
        'title': 'Профиль',
        'form': form,
    }
    return render(request, 'users/profile.html', context)
=======

    context = {
        "title": "Профиль",
        'form': form,
        'baskets': Basket.objects.filter(user=request.user).all() #только корзину юзера
    }

    return render(request, 'users/profile.html', context=context)


def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('products:index'))
>>>>>>> after_pause
