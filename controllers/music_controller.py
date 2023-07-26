from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Artist, Song


music_blueprint = Blueprint("music", __name__)

@music_blueprint.route('/music')
def music():
    artists = Artist.query.all()
    songs = Song.query.all()
    return render_template("music/index.jinja", artists=artists, songs=songs)

@music_blueprint.route('/music', methods=['POST'])
def new_artist():
    artist_name = request.form['artist_name']
    alive = 'alive' in request.form
    new_artist = Artist(artist_name = artist_name, alive = alive )
    db.session.add(new_artist)
    db.session.commit()


    return redirect('/music')

@music_blueprint.route('/music/new_artist')
def new_artist_page():
    return render_template("music/new_artist.jinja")

@music_blueprint.route('/music/new_song')
def new_song_page():
    artists = Artist.query.all()
    return render_template("music/new_song.jinja", artists=artists)

@music_blueprint.route('/music/new_song', methods=['POST'])
def new_song():
    title = request.form['title']
    duration = request.form['duration']
    genre = request.form['genre']
    artist_id = int(request.form['artist_id'])
    new_song = Song(title=title, duration=duration, genre=genre, artist_id=artist_id)
    db.session.add(new_song)
    db.session.commit()
    return redirect('/music')

@music_blueprint.route('/music/<id>')
def single_song(id):
    song = Song.query.get(int(id))
    artist = Artist.query.get(song.artist_id)
    return render_template('/music/individual_song.jinja', song=song, artist=artist)

@music_blueprint.route('/music/<id>/edit')
def edit_song_page(id):
    song = Song.query.get(int(id))
    return render_template('music/edit_song.jinja', song=song)
@music_blueprint.route('/music/<id>/edit_song', methods=['POST'])
def edit_song(id):
    song = Song.query.get(int(id))
    title = request.form['title']
    duration = request.form['duration']
    genre = request.form['genre']
    song.title=title
    song.duration=duration
    song.genre=genre
    db.session.commit()
    return redirect('/music')

@music_blueprint.route('/music/<id>/edit_artist')
def edit_artist_page(id):
    artist=Artist.query.get(int(id))
    return render_template('/music/edit_artist.jinja', artist=artist)

@music_blueprint.route('/music/<id>/edit_artist', methods=['POST'])
def edit_artist(id):
    alive = 'alive' in request.form
    artist = Artist.query.get(int(id))
    artist.alive = alive
    db.session.commit()
    return redirect('/music')

@music_blueprint.route('/music/<id>/delete', methods=['POST'])
def delete_song(id):
    song=Song.query.get(int(id))
    db.session.delete(song)
    db.session.commit()
    return redirect('/music')