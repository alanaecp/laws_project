from django.db import models
from datetime import datetime

 ### MEMBERS

class Member(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_professor = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)
    is_undergraduate = models.BooleanField(default=False)

    def __str__(self):
        return self.name