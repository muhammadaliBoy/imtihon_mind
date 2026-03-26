from django.db import models

# Create your models here.

class Jamoa(models.Model):
    fullname = models.CharField()
    role = models.CharField()

class Kurs(models.Model):
    role = models.CharField()
    text = models.CharField()

class Ariza(models.Model):
    fullname = models.CharField()
    phone = models.CharField()
    course_name = models.CharField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname