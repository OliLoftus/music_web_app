DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Album one', 2022, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album two', 2021, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album three', 2018, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Album four', 2000, 3);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);

INSERT INTO artists (name, genre) VALUES ('Pixies', 'rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'jazz');