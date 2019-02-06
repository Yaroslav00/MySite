from django.db import models


class Picture(models.Model):
    name = models.CharField(blank=True, max_length=100)
    author = models.CharField(blank=True, max_length=50)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    file = models.CharField(blank=True, max_length=100)
    


