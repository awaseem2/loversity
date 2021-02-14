from django.db import models

# Create your models here.
class Users(models.Model):
    #when = models.DateTimeField("date created", auto_now_add=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    major = models.CharField(max_length=140)
    
    def __str__(self):
        return self.name
