from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Artist, Song


music_blueprint = Blueprint("music", __name__)

@music_blueprint.route('/music')
def music():
    artists = Artist.query.all()
    return render_template("music/index.jinja", artists=artists)

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