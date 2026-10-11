from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.symbol

class News(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    source = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    published_date = models.DateTimeField(null=True, blank=True)

class StockData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

class Floorsheet(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    buyer_broker = models.IntegerField()
    seller_broker = models.IntegerField()
    quantity = models.IntegerField()
    rate = models.FloatField()
    date = models.DateField()