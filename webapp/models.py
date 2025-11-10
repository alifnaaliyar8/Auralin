from django.db import models

# Create your models here.
class RegisterDB(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Conform_Password = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True, blank=True)