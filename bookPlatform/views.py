from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from urllib import request

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("login")

  else:
    form = UserCreationForm()

  return render(request, 'register.html', {'form': form})


def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      auth_login(request, user)
      return redirect("user_home")

  else:
    form = AuthenticationForm()

  return render(request, 'login.html', {'form': form})


def logout(request):
  logout(request)
  return redirect('login')


def guest_home(request): # this will be the view for guest
  # each listing in the home page will have the name, name of the owner, listing date and avaliability status
  books = Books.objects.exclude(owner=request.user.username)

  return render(request, 'guest_home.html', {'books': books})


@login_required(redirect_field_name="guest_home")
def user_home(request): # this will be the view for the users. Difference is the profile button and lending option
  books = Books.objects.exclude(owner=request.user.username)

  return render(request, 'user_home.html', {'books': books})

def profile(request):
  return "<p> Cant we be friends </p>"