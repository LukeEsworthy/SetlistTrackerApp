from django.db import models
from .event import Event
from .song import Song


class eventSong(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        verbose_name = ("eventSong")
        verbose_name_plural = ("eventSongs")
