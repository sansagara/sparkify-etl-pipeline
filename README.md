# Data Modeling with Postgres: Song Library
> Leonel Atencio

This is an ETL Pipeline designed for startup **Sparkify**, who wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. This project creates a star-schema database from a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


### Schema
Fact and dimension tables were defined for a star schema with an analytic focus.

#### Fact Table
**songplays** - records in log data associated with song plays i.e. records with page NextSong
*songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent*

#### Dimension Tables
**users** - users in the app
*user_id, first_name, last_name, gender, level*

**songs** - songs in music database
*song_id, title, artist_id, year, duration*

**artists** - artists in music database
*artist_id, name, location, lattitude, longitude*

**time** - timestamps of records in songplays broken down into specific units
*start_time, hour, day, week, month, year, weekday*

### Database creation script
A script for creating and recreating the target database is provided for easy editions. Just run ´python create_tables.py´

### ETL Notebook
A Jupiter notebook is provided to document and demonstrate the ETL pipeline, step by step.

### ETL Script
An ETL script automatically loops through the logs and songs directories, transforms the data using Python/Pandas, and inserts it on the star-schema with relationships, where appropriate.

> Note: The data directories include just a sub-set of the files.
