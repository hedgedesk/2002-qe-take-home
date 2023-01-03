from django.db import models

# Create your models here.
class FXSpot(models.Model):
    date = models.DateField()
    currency_pair = models.CharField(max_length=6)
    bid = models.DecimalField(max_digits=10, decimal_places=5)
    ask = models.DecimalField(max_digits=10, decimal_places=5)
    mid = models.DecimalField(max_digits=10, decimal_places=5)
    high = models.DecimalField(max_digits=10, decimal_places=5)
    low = models.DecimalField(max_digits=10, decimal_places=5)
    yesterday = models.DecimalField(max_digits=10, decimal_places=5)

