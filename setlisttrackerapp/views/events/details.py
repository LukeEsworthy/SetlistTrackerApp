import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from setlisttrackerapp.models import Event, Song, EventSong
from ..connection import Connection
from functools import reduce


def get_event(event_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_event
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.user_id,
            e.name,
            e.date,
            e.start_time,
            e.end_time,
            e.location,
            e.duration,
            e.notes,
            es.id,
            es.rating,
            s.id,
            s.title,
            s.artist,
            s.song_length
        FROM setlisttrackerapp_event e
            JOIN setlisttrackerapp_eventsong es ON e.id = es.event_id
            JOIN setlisttrackerapp_song s ON es.song_id = s.id
                WHERE e.id = ?
                """, (event_id,))

        events = db_cursor.fetchall()

        event_groups = {}

        for (event, song) in events:

            if event.id not in event_groups:
                event_groups[event.id] = event
                event_groups[event.id].songs.append(song)

            else:
                event_groups[event.id].songs.append(song)

        return event_groups[event_id]


@login_required
def event_details(request, event_id):
    if request.method == 'GET':
        event = get_event(event_id)

        event.setlist_length = sum(song.song_length for song in event.songs)
        print("setlist length", event.setlist_length)

        template = 'events/detail.html'
        context = {
            'event': event
        }

        return render(request, template, context)


def create_event(cursor, row):
    _row = sqlite3.Row(cursor, row)

    event = Event()
    event.id = _row["id"]
    event.user_id = _row["user_id"]
    event.name = _row["name"]
    event.date = _row["date"]
    event.start_time = _row["start_time"]
    event.end_time = _row["end_time"]
    event.location = _row["location"]
    event.duration = _row["duration"]
    event.notes = _row["notes"]

    event.songs = []

    song = Song()
    song.id = _row["id"]
    song.title = _row["title"]
    song.artist = _row["artist"]
    song.song_length = _row["song_length"]
    song.rating = _row["rating"]

    return (event, song,)
