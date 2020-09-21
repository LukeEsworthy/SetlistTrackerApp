from django.db import models
from .event import Event
from .song import Song


class EventSong(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        verbose_name = ("eventSong")
        verbose_name_plural = ("eventSongs")
