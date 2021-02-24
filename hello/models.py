from django.db import models

from hello.choices import *

# Create your models here.
class Users(models.Model):
    #when = models.DateTimeField("date created", auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    major = models.CharField(max_length=140)
    age = models.IntegerField()
    gender = models.CharField(max_length=140)
    drink = models.BooleanField()
    attractedto = models.CharField(max_length=140)
    distance_campus = models.CharField(max_length=140)
    politics = models.CharField(max_length=140)
    religion  = models.CharField(max_length=140)
    sharereligion = models.CharField(max_length=140)
    social = models.CharField(max_length=140)
    party = models.CharField(max_length=140)
    pastmatches = models.CharField(max_length=64000)
    
    def __str__(self):
        return self.name
