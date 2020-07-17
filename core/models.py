from django.db import models

# Create your models here.

class Url_model(models.Model):
    url = models.CharField(max_length=120)
    code = models.CharField(max_length=5,unique=True)
    timestamp = models.DateField(auto_now_add=True)