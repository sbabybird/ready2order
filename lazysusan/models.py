from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    type = models.IntegerField()
    container = models.IntegerField()

class Type(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=200)


class Container(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=200)
