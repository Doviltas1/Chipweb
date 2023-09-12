from django.db import models
from django.http import request

class Appointment (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta: 
        ordering = ["-sent_date"]

class Cars_Info (models.Model):
    Marke = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Engine = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    kw = models.CharField(max_length=50)
    kWA = models.CharField(max_length=50)
    nM = models.CharField(max_length=50)
    nMA = models.CharField(max_length=50)
    Price = models.CharField(max_length=50)
    Fuel = models.CharField(max_length=50)
 

    