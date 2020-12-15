from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Produckt(models.Model):
    name = models.CharField(max_length=20)
    categories = models.CharField(max_length=20)
    price = models.IntegerField()
    imageUrl = models.CharField(max_length=20)
