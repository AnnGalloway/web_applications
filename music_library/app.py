import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist import *
from lib.artist_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    return '\n'.join([str(album) for album in repo.all()])

@app.route('/albums', methods = ['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    repo.create(Album(None,'Voyager',2022,2))
    return 'Album added successfully'

@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    names_list = [artist.name for artist in artists]
    return ', '.join(names_list)

@app.route('/artists', methods = ['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    repo.create(Artist(None,request.form['name'], request.form['genre']))
    return 'Artist added successfully'

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

