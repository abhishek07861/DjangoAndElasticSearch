from django.db import models

# Create your models here.


class ElasticSearchDemo(models.Model):
    title = models.CharField(max_length=150,blank=True,null=True)
    content = models.TextField()