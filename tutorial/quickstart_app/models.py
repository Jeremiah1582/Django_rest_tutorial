from django.db import models

# Create your models here.
class Location(models.Model): 
    country= models.CharField(max_length = 50)
    city = models.CharField(max_length= 50)
    road = models.CharField(max_length=50)
    number = models.IntegerField()
    postcode = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'Location'
       
    
    