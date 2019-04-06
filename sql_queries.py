# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id SERIAL, 
    start_time TIMESTAMP NOT NULL,
    user_id INTEGER NOT NULL, 
    level VARCHAR(10) NOT NULL, 
    song_id VARCHAR(20), 
    artist_id VARCHAR(20), 
    session_id INTEGER NOT NULL, 
    location VARCHAR(50) NOT NULL, 
    user_agent VARCHAR(150) NOT NULL
)
""")

user_table_create = ("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY, 
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    gender CHAR(1) NOT NULL, 
    level VARCHAR(10) NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id VARCHAR(20) PRIMARY KEY, 
    title VARCHAR(100) NOT NULL, 
    artist_id VARCHAR(20) NOT NULL, 
    year INT NOT NULL, 
    duration NUMERIC(10,5) NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id VARCHAR(20) PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    latitude NUMERIC(10,5), 
    longitude NUMERIC(10,5)
)
""")

time_table_create = ("""
CREATE TABLE time (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    week INTEGER NOT NULL, 
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday INTEGER NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, songs.artist_id 
FROM songs LEFT JOIN artists ON (songs.artist_id = artists.artist_id)
WHERE songs.title = %s 
AND artists.name = %s 
AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]