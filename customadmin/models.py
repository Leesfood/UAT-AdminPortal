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

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# models.py
class Section(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='sections')

class Employee(models.Model):
    employee_id = models.CharField(max_length=100, unique=True)
    employee_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    email_approver_l1 = models.EmailField(blank=True)
    email_approver_l2 = models.EmailField(blank=True)
    email_approver_l3 = models.EmailField(blank=True)
    approver_email = models.EmailField()
    aknowledge_by = models.TextField(help_text="Multiple emails separated by semicolon (;)")

    # Foreign keys
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # Ensure this exists
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    allow_date = models.IntegerField(help_text="Allowed days of leave")

    def __str__(self):
        return self.employee_name