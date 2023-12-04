from lib.album import *

album = Album(1,"Test Album", 2000, 1)

"""
Album constructs with an id, title and artist_id
"""
def test_album_contructs():
    album = Album(1,"Test Album",2000, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.artist_id == 1

"""
We can format album strings nicely
"""

def test_album_formats_nicely():
    assert str(album) == "Album(1, Test Album, 2000, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1,"Test Album", 2000, 1)
    album2 = Album(1,"Test Album", 2000, 1)
    assert album1 == album2