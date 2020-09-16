import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setlisttrackerapp.models import Song
from ..connection import Connection


def get_songs():
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
        """)

        return db_cursor.fetchall()


@login_required
def song_form(request):
    if request.method == 'GET':
        songs = get_songs()
        template = 'songs/form.html'
        context = {
            'all_songs': songs
        }

        return render(request, template, context)
