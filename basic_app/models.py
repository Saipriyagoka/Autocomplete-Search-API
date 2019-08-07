
from django.db import models

# Create your models here.
class Movie_detail(models.Model):
    name     = models.CharField(max_length = 264)
    titleid  = models.CharField(max_length = 264)
    rating   = models.FloatField()
    cast     = models.CharField(max_length = 264)
    
    def __str__(self):
        return self.name
