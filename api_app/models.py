from django.db import models

class employee(models.Model):
    ename = models.CharField(max_length=100)
    esal = models.IntegerField()
    eadd = models.TextField()
