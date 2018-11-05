from django.db import models
from datetime import datetime

 ### PUBLICATIONS

class Publication(models.Model):
    title = models.CharField(max_length=200)
    abstract_pt = models.TextField(blank=True)
    abstract_en = models.TextField(blank=True)
    link = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title