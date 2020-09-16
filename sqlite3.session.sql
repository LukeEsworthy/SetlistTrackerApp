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
--     (name, date, start_time, end_time, location, duration, notes, user_id_id)
-- VALUES
--     ("Connor's FOMO Pool Party", "2020-09-12", "19:00", "02:00", "1234 Winners Way", 5, "", 1);

-- INSERT INTO setlisttrackerapp_event
--     (name, date, start_time, end_time, location, duration, notes, user_id_id)
-- VALUES
--     ("Tomorrowland: 2021", "2021-07-16", "01:00", "23:59", "Boom, Belgium", 20, "", 1);



-- EVENTSONGS

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id_id, song_id_id)
VALUES
    (4, 1, 1);

INSERT INTO setlisttrackerapp_eventsong
    (rating, event_id_id, song_id_id)
VALUES
    (5, 1, 2);