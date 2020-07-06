from django.db import models

# Create your models here.
class products(models.Model):

    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    objects = models.Manager()
    