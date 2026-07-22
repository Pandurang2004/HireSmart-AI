from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful.")
            return redirect("login")

    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        return redirect("login")

    return render(request, "accounts/login.html")