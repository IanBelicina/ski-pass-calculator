from django.db import models

class Resort(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    ikon = models.BooleanField()
    epic = models.BooleanField()
    avg_day_price = models.PositiveBigIntegerField()
