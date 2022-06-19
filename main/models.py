import email
from pickle import FALSE
from statistics import mode
from django.db import models

# Create your models here.



class Users(models.Model):
    email = models.CharField(max_length=255, primary_key=True, null=False)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class Lessee(models.Model):
    id = models.AutoField( primary_key=True)
    #useremail = models.ForeignKey(Users, on_delete=models.CASCADE)
    #carreg = models.ForeignKey(Cars,on_delete=models.CASCADE)