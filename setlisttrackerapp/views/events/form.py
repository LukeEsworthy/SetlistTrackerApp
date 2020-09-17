import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setlisttrackerapp.models import Event
from ..connection import Connection


def get_events():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            e.id,
            e.user_id,
            e.name,
            e.date,
            e.start_time,
            e.end_time,
            e.location,
            e.duration,
            e.notes
        from setlisttrackerapp_event e
        """)

        return db_cursor.fetchall()


@login_required
def event_form(request):
    if request.method == 'GET':
        events = get_events()
        template = 'events/form.html'
        context = {
            'all_events': events
        }

        return render(request, template, context)
