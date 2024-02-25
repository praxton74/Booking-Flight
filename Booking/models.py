import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):
    code=models.CharField(max_length=10)
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    available=models.IntegerField(default=60)
    booked=models.IntegerField(default=0)
    deleted=models.IntegerField(default=0)
    exists=models.IntegerField(default=0)

    def __str__(self):
        return str(f"{self.code} [{self.origin} - {self.destination}]")

class Ticket(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(default='youremail@namespace.com')
    contact=models.CharField(max_length=10)
    address=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    deleted=models.IntegerField(default=0)

    def __str__(self):
        return str(f"{self.flight.code} - {self.first_name} {self.last_name}")
