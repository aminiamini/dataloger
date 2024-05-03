from django.db import models

class Data(models.Model):
    temprature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    time = models.DateTimeField(null=False, blank=True)
