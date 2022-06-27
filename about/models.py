from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2555, null=True)
    contact = models.IntegerField()
    email = models.CharField(max_length=255, null=True)


class Team(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=1255)
    image = models.ImageField(upload_to='pics')
