# customadmin/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'site' 