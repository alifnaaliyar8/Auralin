from django.db import models

# Create your models here.
class RegisterDB(models.Model):
    User_Name = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Conform_Password = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True, blank=True)

class ContactDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(null=True, blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.TextField(null=True, blank=True)

class CartDB(models.Model):
    User_Name =models.CharField(max_length=50,null=True,blank=True)
    Perfume_Name =models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.PositiveIntegerField()
    Price =  models.PositiveIntegerField()
    Total_Price = models.PositiveIntegerField()
    Perfume_Image = models.ImageField(upload_to="Cart Images", null=True, blank=True)

class OrderDB(models.Model):
    First_Name =models.CharField(max_length=50,null=True,blank=True)
    Last_Name =models.CharField(max_length=50,null=True,blank=True)
    Address = models.TextField(null=True, blank=True)
    Place =models.CharField(max_length=50,null=True,blank=True)
    Post_Code = models.PositiveIntegerField()
    Phone = models.PositiveIntegerField()
    Email = models.EmailField(null=True, blank=True)
    Total_Price =models.PositiveIntegerField()