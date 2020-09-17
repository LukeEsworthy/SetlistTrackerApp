import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from setlisttrackerapp.models import Event
from ..connection import Connection


def get_event(event_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
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
            e.notes
        from setlisttrackerapp_event e
        WHERE e.id = ?
        """, (event_id,))

        return db_cursor.fetchone()


@login_required
def event_details(request, event_id):
    if request.method == 'GET':
        event = get_event(event_id)

        template = 'events/detail.html'
        context = {
            'event': event
        }

        return render(request, template, context)
