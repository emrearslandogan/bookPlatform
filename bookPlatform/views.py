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

  return render(request, 'register.html', {'form': form, "logged_in": 0})


def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      auth_login(request, user)
      return redirect("home")

  else:
    form = AuthenticationForm()

  return render(request, 'login.html', {'form': form, "logged_in": 0})


def logout(request):
  logout(request)
  return redirect('login')


def home(request): # this will be the view for guest
  # each listing in the home page will have the name, name of the owner, listing date and avaliability status
  if not request.user.is_authenticated:
    books = Books.objects.all()
    return render(request, 'guest_home.html', {'books': books, "logged_in": 0})

  else:
    books = Books.objects.exclude(owner=request.user.username)
    return render(request, 'user_home.html', {'books': books, "logged_in": 1})

@login_required(login_url=login)
def profile(request):
  books = Books.objects.filter(owner=request.user.username)
  return render(request, "profile.html", {"books": books, "logged_in": 1})


@login_required(login_url=login)
def add_book(request):
  if request.method == "POST":
    title = request.POST.get("title")
    author = request.POST.get("author")
    year = request.POST.get("year")
    publisher = request.POST.get("publisher")

    if title and author and year:
      Books.objects.create(title=title, author=author, year=int(year), publisher=publisher, owner=request.user.username)
      return redirect("profile")  # Redirect to the homepage after saving

  return render(request, "add_book.html", {"logged_in": 1})


