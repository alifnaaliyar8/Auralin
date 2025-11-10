from django.db import models

# Create your models here.
class FragranceDB(models.Model):
    Fragrance_Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True,blank=True)
    Key_Notes = models.TextField(null=True,blank=True)
    Characteristics = models.TextField(null=True,blank=True)
    Fragrance_Image =models.ImageField(upload_to="Uploads",null=True, blank=True)

class PerfumesDB(models.Model):
    Perfume_Name =models.CharField(max_length=50, null=True, blank=True)
    Brand_Name = models.CharField(max_length=50, null=True, blank=True)
    Fragrance_Category = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(null=True,blank=True)
    Price = models.PositiveIntegerField()
    Expiry_Date = models.DateField(null=True, blank=True)
    Size = models.CharField(max_length=50, null=True, blank=True)
    Perfume_Image =models.ImageField(upload_to="Uploads", null=True,blank=True)



