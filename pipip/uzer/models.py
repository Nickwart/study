from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=75)
    email = models.CharField(max_length=70)
    age = models.IntegerField()

# Create your models here.
