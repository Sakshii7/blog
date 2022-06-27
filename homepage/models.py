from django.db import models


# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    author = models.CharField(max_length=255)


class Destination(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    description = models.CharField(max_length=2555)
    price = models.CharField(max_length=255)
    offer = models.BooleanField(default=False)


class Testimonials(models.Model):
    date = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2555)




