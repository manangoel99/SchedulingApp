from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('User/<int:id>', views.PersonalPage, name="personalPage")
]