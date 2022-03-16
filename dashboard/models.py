
from django.db import models


class client(models.Model):
    firstName= models.CharField(max_length=10, blank=True)
    lastName= models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=30, blank=True)

class hotel(models.Model):
    nameHotel = models.CharField(max_length=20, unique=True, blank=True)
    location = models.CharField(max_length=20, blank=True)

class rooms (models.Model):
    person = models.IntegerField(blank=True)
    image = models.TextField(unique=True, blank=True)
    hotel = models.ForeignKey(hotel,related_name='rooms',on_delete=models.CASCADE)


class reservation(models.Model):
    client = models.ForeignKey(client,related_name='reservation',on_delete=models.CASCADE)
    room = models.ForeignKey(rooms,related_name='reservation',on_delete=models.CASCADE)
    person = models.IntegerField(blank=True)
    dateStart =  models.DateTimeField(auto_now_add=True, blank=True)
    dateEnd = models.TextField(blank=True)
    isReserved = models.BooleanField(default=False, editable=True)


