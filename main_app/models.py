from django.db import models

# Create your models here.

class Nails(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.IntegerField() 

def __str__(self):
    return self.name


