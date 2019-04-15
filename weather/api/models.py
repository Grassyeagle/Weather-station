from django.db import models

# Create your models here.
class Temperature(models.Model):
    celsius = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    record_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.celsius)
    @property
    def fahrenheit(self):
        "Returns the temperature in fahrenheit"
        return '%f' % ((self.celsius * 5/9) +32)




class Humidity(models.Model):
    pass