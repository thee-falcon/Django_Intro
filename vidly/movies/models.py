from django.db import models
from django.utils import timezone

# Create your models here.
class Gener(models.Model):
    name = models.CharField(max_length=255)

class  Movies(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    gener = models.ForeignKey(Gener, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
