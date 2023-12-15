from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

class Measurement(models.Model):
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete = models.CASCADE, related_name='measurments') 
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
       