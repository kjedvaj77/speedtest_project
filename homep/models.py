from django.db import models

# Create your models here.
class SpeedTestResult(models.Model):
    download_speed = models.FloatField()
    upload_speed = models.FloatField()