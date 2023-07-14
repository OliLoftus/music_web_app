from lib.album import Album

""""
Album constructs with an id, title, release_year, artist_id
"""
def test_album_constructs():
    album = Album(1, 'Test Album', 2023, 2)
    assert album.id == 1
    assert album.title == 'Test Album'
    assert album.release_year == 2023
    assert album.artist_id == 2

"""
formatted string
"""

def test_formatted_string():
    album = Album(1, 'Test Album', 2023, 2)
    assert str(album) == 'Test Album, released: 2023, artist: 2'

"""
two identical albums are equal
"""
def test_albums_are_equal():
    album1 = Album(1, 'Test Album', 2023, 2)
    album2 = Album(1, 'Test Album', 2023, 2)
    assert album1 == album2

"""
We can assess an album for validity
"""
def test_album_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "Title", "", "").is_valid() == False
    assert Album(1, "", "Release year", "").is_valid() == False
    assert Album(1, "", "", "Artist id").is_valid() == False
    assert Album(1, "Title", None, "Artist id").is_valid() == False
    assert Album(1, None, "Release year", "Artist id").is_valid() == False
    assert Album(1, "Title", "Release year", None).is_valid() == False
    assert Album(1, "Title", "Release year", "Artist id").is_valid() == True
    assert Album(None, "Title", "Release year", "Artist id").is_valid() == True

"""
We can generate errors for an invalid Album
"""
def test_Album_errors():
    assert Album(1, "", "", "Artist id").generate_errors() == "Title can't be blank, Release year can't be blank"
    assert Album(1, "Title", "", "Artis id").generate_errors() == "Release year can't be blank"
    assert Album(1, "", "Release year", "Artist id").generate_errors() == "Title can't be blank"
    assert Album(1, "Title", None, "Artist id").generate_errors() == "Release year can't be blank"
    assert Album(1, None, "Release year", "Artist id").generate_errors() == "Title can't be blank"
    assert Album(1, "Title", "Release year", "Artist id").generate_errors() == None
    assert Album(None, "Title", "Release year", "Artist id").generate_errors() == None