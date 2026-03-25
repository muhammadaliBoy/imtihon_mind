from django.db import models

# Create your models here.

class Jamoa(models.Model):
    fullname = models.CharField()
    role = models.CharField()

class Kurs(models.Model):
    role = models.CharField()
    text = models.CharField()
