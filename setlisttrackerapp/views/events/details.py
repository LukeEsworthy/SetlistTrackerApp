import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import math
from setlisttrackerapp.models import Event, Song, EventSong
from setlisttrackerapp.views import song_list_search
from ..connection import Connection


def get_event(event_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_event
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id as event_id,
            e.user_id,
            e.name,
            e.date,
            e.start_time,
            e.end_time,
            e.location,
            e.duration,
            e.notes,
            es.id as event_song_id,
            es.rating,
            s.id as song_id,
            s.title,
            s.artist,
            s.song_length
        FROM setlisttrackerapp_event e
            LEFT JOIN setlisttrackerapp_eventsong es ON e.id = es.event_id
            LEFT JOIN setlisttrackerapp_song s ON es.song_id = s.id
        WHERE e.id = ?
                """, (event_id,))

        events = db_cursor.fetchall()

        event_groups = {}

        for (event, song) in events:

            if event.id not in event_groups:
                event_groups[event.id] = event
                if song is not None:
                    event_groups[event.id].songs.append(song)

            else:
                if song is not None:
                    event_groups[event.id].songs.append(song)

    return event_groups[event_id]


@login_required
def event_details(request, event_id):
    if request.method == 'GET':
        event = get_event(event_id)
        event.setlist_length = sum(song.song_length for song in event.songs)
        event.duration_seconds = (event.duration * 60 * 60)
        event.setlist_length_minutes = math.floor(event.setlist_length / 60)
        event.setlist_length_seconds = (event.setlist_length % 60)
        event.setlist_remaining_time_raw = (
            event.duration_seconds - event.setlist_length)
        event.setlist_remaining_minutes = math.floor(
            event.setlist_remaining_time_raw / 60)
        event.setlist_remaining_seconds = (
            event.setlist_remaining_time_raw % 60)

        if request.GET.get("query") is not None:
            results = song_list_search(request)

            template = 'events/detail.html'
            context = {
                'event': event,
                'search_songs': results
            }

        else:
            template = 'events/detail.html'
            context = {
                'event': event
            }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
                and form_data["actual_method"] == "PUT"):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE setlisttrackerapp_event
                SET name = ?,
                    date = ?,
                    start_time = ?,
                    end_time = ?,
                    location = ?,
                    duration = ?,
                    notes = ?
                WHERE id = ?
                """,
                                  (
                                      form_data['name'], form_data['date'], form_data['start_time'], form_data[
                                          'end_time'], form_data['location'], form_data['duration'], form_data['notes'], event_id,
                                  ))

            return redirect(reverse('setlisttrackerapp:event', kwargs={"event_id": event_id}))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM setlisttrackerapp_event
                WHERE id = ?
                """, (event_id,))

            return redirect(reverse('setlisttrackerapp:events'))

        if ("song_id" in form_data):
            # SQL query for creating the eventSong table
            # song_id and event_id
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                INSERT INTO setlisttrackerapp_eventSong
                (event_id, song_id)
                VALUES
                (?, ?)
                """, (event_id, form_data["song_id"]))

            return redirect(reverse('setlisttrackerapp:event', kwargs={"event_id": event_id}))


def create_event(cursor, row):
    _row = sqlite3.Row(cursor, row)

    event = Event()
    event.id = _row["event_id"]
    event.user_id = _row["user_id"]
    event.name = _row["name"]
    event.date = _row["date"]
    event.start_time = _row["start_time"]
    event.end_time = _row["end_time"]
    event.location = _row["location"]
    event.duration = _row["duration"]
    event.notes = _row["notes"]

    event.songs = []
    if _row["song_id"] is not None:
        song = Song()
        song.id = _row["song_id"]
        song.title = _row["title"]
        song.artist = _row["artist"]
        song.song_length = _row["song_length"]
        song.rating = _row["rating"]

        return (event, song,)

    else:
        song = None
        return (event, song,)
