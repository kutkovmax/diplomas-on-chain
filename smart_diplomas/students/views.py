from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm, StudentLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, "profile.html")


def register_view(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("issue_certificate")
    else:
        form = StudentRegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("issue_certificate")
    else:
        form = StudentLoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
