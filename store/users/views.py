from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
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


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
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

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Профиль',
        'form': form,
    }
    return render(request, 'users/profile.html', context)