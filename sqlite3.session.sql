-- SONGS

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Infinity 2008", "Guru Josh Project", 191);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Satisfaction", "Benny Benassi", 147);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Call On Me", "Eric Prydz", 175);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Better Off Alone", "Alice DJ", 176);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Around the World", "Daft Punk", 242);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Kernkraft 400", "Zombie Nation", 211);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Blue (Da Ba Dee)", "Eiffel 65", 229);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Faded", "Zhu", 254);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("Toulouse", "Nicky Romero", 216);

INSERT INTO setlisttrackerapp_song
    (title, artist, song_length)
VALUES
    ("What Is Love", "Haddaway", 241);



-- EVENTS

-- INSERT INTO setlisttrackerapp_event
--     (name, date, start_time, end_time, location, duration, notes, user_id)
-- VALUES
--     ("Connor's FOMO Pool Party", "2020-09-12", "19:00", "02:00", "1234 Winners Way", 5, "", 1);

-- INSERT INTO setlisttrackerapp_event
--     (name, date, start_time, end_time, location, duration, notes, user_id)
-- VALUES
--     ("Tomorrowland: 2021", "2021-07-16", "01:00", "23:59", "Boom, Belgium", 20, "", 1);



-- EVENTSONGS for EVENT 1

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (4, 1, 1);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (5, 1, 2);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (2, 1, 3);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (3, 1, 4);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (4, 1, 5);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (5, 1, 6);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (1, 1, 7);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (5, 1, 8);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (2, 1, 9);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (3, 1, 10);


-- EVENTSONGS for EVENT 2

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (5, 2, 1);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (4, 2, 2);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (3, 2, 3);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (2, 2, 4);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (1, 2, 5);


-- EVENTSONGS for EVENT 4

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (1, 4, 5);


-- EVENTSONGS for EVENT 5

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id, song_id)
VALUES
    (1, 5, 5);



-- Testing EVENT DETAIL with eventSongs

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
WHERE e.id = 1;

