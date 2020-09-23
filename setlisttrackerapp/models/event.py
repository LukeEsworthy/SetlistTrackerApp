from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(blank=False, max_length=75)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    end_time = models.TimeField(blank=False)
    location = models.CharField(blank=False, max_length=100)
    duration = models.IntegerField(blank=False)
    notes = models.CharField(blank=False, max_length=500)

    class Meta:
        verbose_name = ("event")
        verbose_name_plural = ("events")

    def __str__(self):
        return self.name
