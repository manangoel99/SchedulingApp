from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == "POST":
        if "SignIn" in request.POST:
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
            print(user)
            if user is not None:
                return redirect(PersonalPage, user.pk)
            else:
                return render(request, template_name="index.html")
        if "SignUp" in request.POST:
            u = User(username=request.POST["username"], first_name=request.POST["name"], email=request.POST["email"])
            u.set_password(request.POST["password"])
            User.save(u)
            login(request, u)
            return redirect(PersonalPage, u.pk)
    return render(request, template_name="index.html")

@login_required(login_url="")
def PersonalPage(request, id):
    return render(request, template_name="UserHome.html")