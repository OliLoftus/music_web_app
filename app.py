import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# music_library routes

# @app.route('/albums', methods=['POST'])
# def post_albums():
#     # if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
#     #     return 'You need to submit a title, release_year and artist_id.', 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None,
#         request.form['title'],
#         request.form['release_year'],
#         request.form['artist_id'])
#     repository.create(album)
#     return 'Album added successfully.'

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    # result_string = ""
    # for album in albums:
    #     result_string += str(f"{album}\n")
    # return result_string
    return render_template('albums/index.html', albums=albums)

#GET /albums/id

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('albums/show.html', album=album)

# GET /albums/new
# Returns a form to create a new album
@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')


# POST /albums
# Creates a new book
@app.route('/albums', methods=['POST'])
def create_album():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    # Create an album object
    album = Album(None, title, release_year, artist_id)

    # Check for validity and if not valid, show the form again with errors
    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

    # Save the album to the database
    album = repository.create(album)

    # Redirect to the book's show route to the user can see it
    return redirect(f"/albums/{album.id}")


# GET /artists

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    # result_string = ""
    # for artist in artists:
    #     print(artist)
    #     result_string += f"{artist.id}. {artist.name} "
    # return result_string
    return render_template('/artists/index.html', artists=artists)

#GET /artists/<id>

@app.route('/artists/<int:id>')
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artists/show.html', artist=artist)

# POST /artists

# @app.route('/artists', methods=['POST'])
# def post_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = Artist(
#         None,
#         request.form['name'],
#         request.form['genre'],)
#     repository.create(artist)
#     return ''

# GET /artists/new
# Returns a form to create a new artist
@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new.html')


# POST /artist
# Creates a new artist
@app.route('/artists', methods=['POST'])
def create_artist():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    # Get the fields from the request form
    name = request.form['name']
    genre = request.form['genre']

    # Create an artist object
    artist = Artist(None, name, genre)

    # Check for validity and if not valid, show the form again with errors
    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400

    # Save the artist to the database
    artist = repository.create(artist)

    # Redirect to the artist's show route to the user can see it
    return redirect(f"/artists/{artist.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
