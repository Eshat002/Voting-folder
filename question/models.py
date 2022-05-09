from pyexpat import model
from sqlite3 import Timestamp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    question=models.CharField(null=True,blank=True,max_length=200)
    imageA=models.ImageField()
    imageB=models.ImageField()
    countA=models.ManyToManyField(User,related_name="count_A")
    countB=models.ManyToManyField(User,related_name="count_B")
    timestamp=models.DateTimeField(auto_now_add=True)


