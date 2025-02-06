from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

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
      return redirect("home")

  else:
    form = AuthenticationForm()

  return render(request, 'login.html', {'form': form})

def logout(request):
  logout(request)
  return redirect('login')