from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event
from datetime import datetime as present
import threading
import smtplib
import pytz


def send_mail():
    threading.Timer(60.0, send_mail).start()



    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    try:
        s.login("enter_email_id", "enter_password")

        for event in Event.objects.all():
            now = present.utcnow().replace(tzinfo=pytz.utc)
            timediff = event.datetime - now

            print(timediff.total_seconds())
            if timediff.total_seconds() < 920 and timediff.total_seconds > 880:
                message = "Hey " + event.user.first_name + "<br>" + " You have an upcoming titled "+ event.title+ " at "+ str(event.datetime)+ "<br>"+ " Please reach the venue: "+ event.venue+ " on time." 
                s.sendmail("enter_email_id", event.user.email, message)
    except:
        pass
    s.quit()

send_mail()

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect(PersonalPage, request.user.pk)
    if request.method == "POST":
        if "SignIn" in request.POST:
            user = authenticate(username=request.POST["username"], password=request.POST["password"])
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
    # print(Event.objects.filter(user=request.user))
    UpcomingList = []
    GoneList = []
    for ev in Event.objects.filter(user=request.user).order_by('datetime'):
        if ev.datetime >= timezone.now():
            UpcomingList.append(ev)
        else:
            GoneList.append(ev)
    return render(request, template_name="UserHome.html", context={
        "EventsUpcoming" : UpcomingList,
        "EventsGone" : GoneList,
    })

@login_required(login_url="")
def AddEvent(request):
    if request.method == "POST":
        event = Event(user=request.user, datetime=request.POST["datetime"], description=request.POST["description"], venue=request.POST["Venue"], title=request.POST["Name"], phoneNumber=request.POST["Phone Number"])
        event.save()
        print(event.user)
        return redirect(PersonalPage, request.user.pk)

@login_required(login_url="")
def EditEvent(request, id):
    if request.method == "GET":
        return render(request, template_name="EventPage.html", context={
            "event" : Event.objects.get(pk=id)
        })
    if request.method == "POST":
        event = Event.objects.get(pk=id)
        event.title = request.POST["Name"]
        event.venue = request.POST["Venue"]
        event.phoneNumber = request.POST["Phone Number"]
        event.datetime = request.POST["datetime"]
        event.description = request.POST["description"]
        event.save()
        return redirect(PersonalPage, request.user.pk)

@login_required(login_url="")
def DeleteEvent(request, id):
    event = Event.objects.get(pk=id)
    event.delete()

    return JsonResponse({
        "deleted" : True
    })

@login_required(login_url="")
def LogOut(request):
    logout(request)
    return redirect(index)
