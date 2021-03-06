from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
timings = (('1','9:30'),('2','11:30'),('3','14:30'))

class BookingListIndi(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name_person = models.CharField(max_length=200)
    industry_name = models.CharField(max_length=100)
    email=models.EmailField(null=True)
    date_visit = models.DateField(default=timezone.now)
    slot_time = models.CharField(max_length=10, choices=timings, default='9:30')
    visiting_members = models.IntegerField(default=0)
    total_available = models.IntegerField(default=20)
    total_taken = models.IntegerField(default = 0)
    street_name = models.CharField(max_length=150)
    city_name = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    code = models.CharField(max_length=20)
    visited = models.BooleanField(default=False)

class BookingListOrga (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name_person = models.CharField(max_length=200)
    organisation_name = models.CharField(max_length=200)
    industry_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_visit = models.DateField(default=timezone.now)
    slot_time = models.CharField(max_length=10, choices=timings, default='9:30')
    visiting_members = models.IntegerField(default=0)
    total_available = models.IntegerField(default=20)
    total_taken = models.IntegerField(default = 0)
    street_name = models.CharField(max_length=150)
    city_name = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    code = models.CharField(max_length=20)
    visited = models.BooleanField(default=False)

class Tickets(models.Model):
    day = models.DateField()
    slot = models.CharField(max_length = 10)
    ticks = models.IntegerField(default = 20)
