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

"""
We can assess an album for validity
"""
def test_artist_validity():
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "Artist", "").is_valid() == False
    assert Artist(1, "", "genre").is_valid() == False
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "Artist", None).is_valid() == False
    assert Artist(1, None, "genre").is_valid() == False
    assert Artist(1, "Artist", "genre").is_valid() == True
    assert Artist(None, "Artist", "genre",).is_valid() == True

"""
We can generate errors for an invalid Artist
"""
def test_artist_errors():
    assert Artist(1, "", "").generate_errors() == "Artist can't be blank, Genre can't be blank"
    assert Artist(1, "Artist", "").generate_errors() == "Genre can't be blank"
    assert Artist(1, "", "genre").generate_errors() == "Artist can't be blank"
    assert Artist(1, "Artist", None).generate_errors() == "Genre can't be blank"
    assert Artist(1, None, "genre").generate_errors() == "Artist can't be blank"
    assert Artist(1, "Artist", "genre").generate_errors() == None
    assert Artist(None, "Artist", "genre").generate_errors() == None