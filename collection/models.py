from datetime import timezone

from django.db import models

# Create your models here.
from django.utils.timezone import now


class Material(models.Model):
    metal = models.CharField(max_length=10,default="")
    rate = models.IntegerField()
    def __str__(self):
        return  self.metal

class Item(models.Model):
    name = models.CharField(max_length=25,default="",primary_key=True)
    weight = models.FloatField(verbose_name='weigth(gms)')
    def __str__(self):
        return  self.name

class Order(models.Model):
    customername = models.CharField(max_length=25,default="")
    item = models.ManyToManyField(Item)
    metal = models.ForeignKey(Material,on_delete=models.CASCADE)
    price = models.IntegerField()
    place = models.CharField(max_length=25)
    orderdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.customername