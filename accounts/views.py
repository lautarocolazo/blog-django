from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def register_page(request):
    """
    Rendering register page
    """
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "registration/signup.html", context)


def login_page(request):
    """
    Rendering login page
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("Invalid password or user")

    context = {}
    return render(request, "registration/login.html", context)


def logout_user(request):
    """
    Logout user function
    """
    logout(request)
    return redirect("login")
