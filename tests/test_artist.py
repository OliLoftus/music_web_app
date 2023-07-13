from lib.artist import Artist

"""
test artist constructs with relevant properties
"""
def test_artist_constructs():
    artist = Artist(1, 'test name', 'test genre')
    assert artist.id == 1
    assert artist.name == 'test name'
    assert artist.genre == 'test genre'

"""
We can compare two identical artists and they 
are equal
"""
def test_artist_equality():
    artist1 = Artist(1, 'test name', 'test genre')
    artist2 = Artist(1, 'test name', 'test genre')
    artist1 == artist2

"""
format artist to string
"""
def test_format_artist_to_string():
    artist = Artist(1, 'test name', 'test genre')
    assert str(artist) == "test name, genre: test genre"