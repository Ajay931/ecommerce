from django.db import models

# Create your models here.
class item(models.Model):
    username = models.CharField(max_length=30)
    pro1 = models.CharField(max_length=30)
    pro2 = models.CharField(max_length=30)
    pro3 = models.CharField(max_length=30)
    objects = models.Manager()

   

