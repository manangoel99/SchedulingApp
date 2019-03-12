from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=300)
    venue = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()