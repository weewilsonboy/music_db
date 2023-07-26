from app import db

class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(64))
    alive = db.Column(db.Boolean)
    songs = db.relationship('Song', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id}: {self.artist_name} {self.alive}>'
    
class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    genre = db.Column(db.String(64))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    def __repr__(self):
        return f'<Song {self.id}: {self.title}>'

