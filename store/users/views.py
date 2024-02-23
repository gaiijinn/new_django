from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


from users.models import User
from users.forms import UserLoginForm


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
    return render(request, 'users/registration.html')