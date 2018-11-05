from django.db import models
from datetime import datetime

 ### PROJECT

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title