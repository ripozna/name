from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
