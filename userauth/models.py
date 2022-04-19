
from operator import mod
from pyexpat import model
from unittest.mock import DEFAULT
from django.db import models
from django.contrib.auth.models import User

class hotel(models.Model):
    nameHotel = models.CharField(max_length=20, unique=True, blank=True)
    location = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=300, blank=True)
    stars = models.IntegerField(blank=True)
    def __str__(self) -> str:
        return self.nameHotel

class rooms (models.Model):
    person = models.IntegerField(blank=True)
    image = models.TextField(unique=True, blank=True)
    hotel = models.ForeignKey(hotel,on_delete=models.CASCADE)   

class reservation(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(rooms,on_delete=models.CASCADE)
    person = models.IntegerField(blank=True)
    dateStart =  models.DateTimeField(auto_now_add=True, blank=True)
    dateEnd = models.TextField(blank=True)
    isReserved = models.BooleanField(default=False, editable=True)


