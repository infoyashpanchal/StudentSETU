from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    fname = models.CharField(max_length = 20, default="",null=True,blank=True)
    lname = models.CharField(max_length = 20, default="",null=True,blank=True)
    category = models.CharField(max_length = 10, default="Student",null=True,blank=True)
    gender = models.CharField(max_length = 15, default="",null=True,blank=True)
    department = models.CharField(max_length = 30, default="",null=True,blank=True)
    Class = models.CharField(max_length = 15, default="",null=True,blank=True)
    email = models.EmailField(max_length = 30, default="",null=True,blank=True)
    password = models.CharField(max_length = 30, default="",null=True,blank=True)
    re_password = models.CharField(max_length = 30, default="",null=True,blank=True)
    