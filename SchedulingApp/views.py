from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == "POST":
        if "SignIn" in request.POST:
            print(request.POST)
        if "SignUp" in request.POST:
            u = User(username=request.POST["username"], first_name=request.POST["name"], password=request.POST["password"], email=request.POST["email"])
            User.save(u)
            login(request, u)
            return redirect(PersonalPage, u.pk)
    return render(request, template_name="index.html")

@login_required(login_url="")
def PersonalPage(request, id):
    return render(request, template_name="UserHome.html")