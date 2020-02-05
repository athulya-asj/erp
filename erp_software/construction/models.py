from django.db import models
from django import forms


# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=200)
    password =models.CharField(max_length=200)
class contractor_registration(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField(null="True",blank="True")
    password=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="Available")
class employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.IntegerField(null="True",blank="True")
    nid=models.CharField(max_length=200)
    salary=models.IntegerField(null="True",blank="True")
    grade=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="Available")
class work(models.Model):
    name=models.CharField(max_length=200)
    phone=models.IntegerField(null="True",blank="True")
    type=models.CharField(max_length=200)
    fromdate=models.CharField(max_length=200)
    todate=models.CharField(max_length=200)
    budget=models.CharField(max_length=200)
    enumber=models.CharField(max_length=200)
    contractor=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="pending")
class select_employee(models.Model):
    wid=models.IntegerField()
    eid=models.IntegerField()

