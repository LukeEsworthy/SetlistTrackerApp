from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=75)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    duration = models.IntegerField()
    notes = models.CharField(max_length=500)

    class Meta:
        verbose_name = ("event")
        verbose_name_plural = ("events")

    def __str__(self):
        return self.name
