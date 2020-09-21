# import sqlite3
# from django.shortcuts import render
# from setlisttrackerapp.models import eventSong
# from ..connection import Connection


# def eventSong_list(event_id):
#     if request.method == 'GET':
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()

#             db_cursor.execute("""
#             select
#                 es.id,
#                 es.event_id,
#                 es.song_id,
#                 es.rating,
#                 s.title,
#                 s.artist,
#                 s.song_length
#             from setlisttrackerapp_eventSong es
#             join setlisttrackerapp_song s on es.song_id = s.id
#             join setlisttrackerapp_event e on es.event_id = e.id
#             where e.id = ?
#             """, (event_id,))

#             all_eventSongs = []
#             dataset = db_cursor.fetchall()

#             for row in dataset:
#                 eventSong = EventSong()
#                 eventSong.id = row['id']
#                 eventSong.event_id = row['event_id']
#                 eventSong.song_id = row['song_id']
#                 eventSong.rating = row['rating']
#                 eventSong.title = row['title']
#                 eventSong.artist = row['artist']
#                 eventSong.song_length = row['song_length']

#                 all_eventSongs.append(eventSong)

#         template = 'events/detail.html'
#         context = {
#             'all_eventSongs': all_eventSongs
#         }

#         return render(request, template, context)
