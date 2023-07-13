from lib.artist import Artist
from lib.artist_repository import ArtistRepository

"""
When we call ArtistRepository all
we get a list of artist objects returned
"""

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, 'Pixies','rock'),
        Artist(2, 'ABBA', 'pop'),
        Artist(3, 'Taylor Swift', 'pop'),
        Artist(4, 'Nina Simone', 'jazz')
    ]

"""
when we call ArtistRepository create
we get a new artist in the database
"""
def test_create_artist_method(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, 'Wild nothing', 'indie'))

    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies','rock'),
        Artist(2, 'ABBA', 'pop'),
        Artist(3, 'Taylor Swift', 'pop'),
        Artist(4, 'Nina Simone', 'jazz'),
        Artist(5,'Wild nothing', 'indie')
    ]
