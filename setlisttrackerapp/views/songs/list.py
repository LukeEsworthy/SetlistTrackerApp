import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from setlisttrackerapp.models import Song
from ..connection import Connection


@login_required
def song_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                s.id,
                s.title,
                s.artist,
                s.song_length
            from setlisttrackerapp_song s
            order by s.title COLLATE NOCASE ASC
            """)

            all_songs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                song = Song()
                song.id = row['id']
                song.title = row['title']
                song.artist = row['artist']
                song.song_length = row['song_length']

                all_songs.append(song)

        template = 'songs/list.html'
        context = {
            'all_songs': all_songs
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO setlisttrackerapp_song
            (
                title, artist, song_length
            )
            VALUES (?, ?, ?)
            """,
                              (form_data['title'], form_data['artist'],
                               form_data['song_length']))

        return redirect(reverse('setlisttrackerapp:songs'))
