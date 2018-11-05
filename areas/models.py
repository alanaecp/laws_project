from django.db import models
from datetime import datetime

 ### AREA

class Area(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=False)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title