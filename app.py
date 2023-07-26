from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://steph:password@localhost:5432/music_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# from models import Artist
# from models import Song

# @app.route("/")
# def hello_world():
#     ariana = Artist(artist_name="Ariana Grande", alive=True)
#     db.session.add(ariana)
#     db.session.commit()

#     thanku = Song(title="thank u, next", duration=207, genre="Pop", artist_id=1)
#     db.session.add(thanku)
#     db.session.commit()
#     return "hkf"


#     #delete all the rows - below 2 lines will run every time
#     Task.query.delete() #immediately delete 
#     User.query.delete()

#     steve = User(first_name="Steve", last_name="Bootcamp")
#     db.session.add(steve)
#     db.session.commit() #commit. Need this for the updates to users to take effect
#     print("steph after commit")
#     print(steph)

#     #get all the users using below. This is the equivalent to select * from users in sql
#     users = User.query.all()
#     print("get all the users")
#     print(users)
