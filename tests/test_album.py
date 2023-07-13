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