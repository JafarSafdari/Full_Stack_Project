from statistics import mode
from django.db import models
from django.forms import SlugField

# Create your models here.

#each class is a table and each variable is a collom
class Car(models.Model):
    reg = models.CharField(max_length=255, primary_key=True, null=False)
    slug = models.SlugField()
    fabric = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    info = models.TextField()


def __str__(self):
    return self.fabric

def test(self):
    return self.info[:50]