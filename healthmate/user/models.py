from django.db import models

# Create your models here.
class AirQualityIndex(models.Model):
    temperature = models.FloatField(default=0.0)
    humidity = models.FloatField()
    pmTwoPointFive = models.FloatField()
    pmTen = models.FloatField()
    nitrogendioxide = models.FloatField()
    sulphurdioxide = models.FloatField()
    carbonmonxide = models.FloatField()
    Proximity_to_Industrial_Areas = models.FloatField()
    Population_Density = models.IntegerField()