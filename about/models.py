from django.db import models

# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    contact = models.IntegerField()
    email = models.CharField(max_length=255, null=True)


