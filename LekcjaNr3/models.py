from django.db import models

# Create your models here.
class NaszPierwszyModel(models.Model):
    nazwa = models.CharField(max_length=120)
    numer = models.IntegerField()
