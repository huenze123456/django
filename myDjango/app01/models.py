from django.db import models

# Create your models here.
class Test01(models.Model):
    name=models.CharField(max_length=20)
    age =models.CharField(max_length=3)
    tel = models.CharField(max_length=20)