from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Artist, Song


music_blueprint = Blueprint("music", __name__)

@music_blueprint.route("/music")
def music():
    artists = Artist.query.all()
    return render_template("music/index.jinja", artists=artists)