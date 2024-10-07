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

class LeaveType(models.Model):
    name_kh = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name_en  # or return name_kh if you prefer Khmer name

    class Meta:
        db_table = 'LeaveType'