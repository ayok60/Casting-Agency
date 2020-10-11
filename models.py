import os
from sqlalchemy import Column, String, create_engine, Enum
from flask_sqlalchemy import SQLAlchemy
import json

default_path = 'postgres://ayakhashoggi@localhost:5432/db'
database_path = os.getenv('DATABASE_URL',default_path)
#database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movies
Have title and release year
'''
class Movies(db.Model):  
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    release_date = db.Column(db.String)
    image_link = db.Column(db.String(500))


    def __init__(self, title, release_date, image_link):
        self.title = title
        self.release_date = release_date
        self.image_link = image_link

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'image_link': self.image_link
        }

'''
Actors
Have name, age and gender
'''
class Actors(db.Model):  
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    age = db.Column(db.String)
    gender = db.Column(db.Enum('Male', 'Female', name="gender"))
    image_link = db.Column(db.String)

    def __init__(self, name, age, gender , image_link):
        self.name = name
        self.age = age
        self.gender = gender
        self.image_link = image_link

    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'image_link': self.image_link
        }

