from django.db import models

# Create your models here.


class ElasticSearchDemo(models.Model):
    title = models.CharField(max_length=150,blank=True,null=True)
    content = models.TextField()
    
class SateCity(models.Model):
    city = models.CharField(max_length=50,blank=True,null=True)
    growth = models.CharField(max_length=50,blank=True,null=True)
    latitude = models.CharField(max_length=50,blank=True,null=True)
    longitude = models.CharField(max_length=50,blank=True,null=True)
    population = models.PositiveBigIntegerField(blank=True,null=True)
    rank = models.PositiveIntegerField(blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.city