import sqlite3
from django.shortcuts import render
from setlisttrackerapp.models import eventSong
from ..connection import Connection


def eventSong_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                es.id,
                es.event_id,
                es.song_id,
                es.rating,
                s.id,
                s.title,
                s.artist,
                s.song_length
            from setlisttrackerapp_eventSong es
            join setlisttrackerapp_song s on es.song_id = s.id
            """)

            all_eventSongs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                eventSong = EventSong()
                eventSong.id = row['id']
                eventSong.event_id = row['event_id']
                eventSong.song_id = row['song_id']
                eventSong.rating = row['rating']
                

                all_eventSongs.append(eventSong)

        template = 'books/list.html'
        context = {
            'all_eventSongs': all_eventSongs
        }

        return render(request, template, context)
