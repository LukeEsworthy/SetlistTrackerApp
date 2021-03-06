import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from setlisttrackerapp.models import Event
from ..connection import Connection


@login_required
def event_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            user = request.user

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
            where e.user_id = ?
            """, (user.id,))

            all_events = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                event = Event()
                event.id = row['id']
                event.user_id = row['user_id']
                event.name = row['name']
                event.date = row['date']
                event.start_time = row['start_time']
                event.end_time = row['end_time']
                event.location = row['location']
                event.duration = row['duration']
                event.notes = row['notes']

                all_events.append(event)

        template = 'events/list.html'
        context = {
            'all_events': all_events
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO setlisttrackerapp_event
            (
                user_id, name, date,
                start_time, end_time, location, duration, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                              (request.user.id, form_data['name'],
                               form_data['date'], form_data['start_time'], form_data['end_time'], form_data['location'], form_data['duration'], form_data['notes']))

        return redirect(reverse('setlisttrackerapp:events'))
