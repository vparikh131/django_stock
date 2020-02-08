from django.db import models

# Create your models here. These are 
class Stock(models.Model):
    ticker = models.CharField(max_length=10) #field = models.type where CharField is just text

    def __str__(self):
        return self.ticker
