from django.db import models



class Calculation(models.Model):
    name = models.CharField(max_length=200)
    value = models.BigIntegerField()
