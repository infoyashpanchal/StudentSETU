from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    fname = models.CharField(max_length = 20, default="")
    lname = models.CharField(max_length = 20, default="")
    category = models.CharField(max_length = 10, default="Student")
    gender = models.CharField(max_length = 15, default="")
    department = models.CharField(max_length = 30, default="")
    Class = models.CharField(max_length = 15, default="")
    email = models.EmailField(max_length = 30, default="")
    password = models.CharField(max_length = 30, default="")
    re_password = models.CharField(max_length = 30, default="")
    