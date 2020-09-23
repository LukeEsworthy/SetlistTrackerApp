import sqlite3
from django.shortcuts import render
from setlisttrackerapp.models import Song
from ..connection import Connection


def song_list_search(request):
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
            where s.title like ?
            """, ('%'+request.GET.get("query", "")+'%',))

            search_all_songs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                song = Song()
                song.id = row['id']
                song.title = row['title']
                song.artist = row['artist']
                song.song_length = row['song_length']

                search_all_songs.append(song)

        template = 'songs/searchResults.html'
        context = {
            'search_all_songs': search_all_songs
        }

        return render(request, template, context)
