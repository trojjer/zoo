from django.db import models
from django.utils import timezone


class Species(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'animals'


class Animal(models.Model):
    name = models.CharField(max_length=30)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    last_feed_time = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'animals'
