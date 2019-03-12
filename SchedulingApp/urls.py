from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('User/<int:id>', views.PersonalPage, name="personalPage"),
    path('AddEvent', views.AddEvent, name="AddEvent"),
    path('EditEvent/<int:id>', views.EditEvent, name="EditEvent"),
    path('DeleteEvent/<int:id>', views.DeleteEvent, name="DeleteEvent"),
    path('LogOut', views.LogOut, name="logout"),
]