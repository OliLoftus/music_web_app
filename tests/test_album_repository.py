from lib.album import Album
from lib.album_repository import AlbumRepository

"""
When we call all method we get list of album obects
"""
def test_all_method(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, 'Album one', 2022, 1),
        Album(2, 'Album two', 2021, 2),
        Album(3, 'Album three', 2018, 1),
        Album(4, 'Album four', 2000, 3)
    ]

"""
When we call create, we get a new album in
the list
"""
def test_create_method(db_connection):
    db_connection.seed("seeds/album_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, 'Album ten', 2010, 10))

    albums = repository.all()
    
    assert albums == [
        Album(1, 'Album one', 2022, 1),
        Album(2, 'Album two', 2021, 2),
        Album(3, 'Album three', 2018, 1),
        Album(4, 'Album four', 2000, 3),
        Album(5, 'Album ten', 2010, 10)
    ]