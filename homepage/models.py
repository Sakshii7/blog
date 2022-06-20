from django.db import models

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)
