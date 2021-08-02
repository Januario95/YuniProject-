from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate, login, logout
)
from django.contrib.auth.decorators import (
    login_required
)
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import (
    UserRegisterForm, UserLoginForm
)


@login_required
def home(request):
    return render(request,
                  'portal/home.html',
                  {})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']

            user = authenticate(username=username,
                                password=password)

            if user is None:
                messages.warning(request, 'Wrong username or password')
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()

    return render(request,
                  'auth/login.html',
                  {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            del data['password2']
            user = User.objects.create(**data)
            user.save()
            return redirect('/login/')
    else:
        form = UserRegisterForm()

    return render(request,
                  'auth/register.html',
                  {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/login/')
