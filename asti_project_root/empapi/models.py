from django.db import models

from django.db import models

class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    address = models.CharField(max_length=100)
