from django.db import models

# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    page = models.TextField()
