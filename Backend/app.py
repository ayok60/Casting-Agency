import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movies, Actors

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

#  Actors
#  ----------------------------------------------------------------

  @app.route('/actors', methods=['GET'])
  def get_actors():
    
    actors = Actors.query.all()
    actors_lsit = [actor.format() for actor in actors]
    
    return jsonify({
      "success": True, 
      "actors": actors_lsit
    }),200

  @app.route('/actors', methods=['GET','POST'])
  def post_actors():
    
    actor = Actors(
      name = "aya",
      age = 25,
      gender = "Female"
    )
    
    try:
      actor.insert()
    except:
      abort(422)
    
    actors = Actors.query.all()
    actors_lsit = [actor.format() for actor in actors]
    
    return jsonify({
      "success": True, 
      "actor": actor.format(),
      "actors": actors_lsit
    }),200

  @app.route('/actors/<int:id>', methods=['PATCH', 'GET'])
  def edit_actors(id):
    
    actors = Actors.query.all()
    actors_lsit = [actor.format() for actor in actors]

    actor = Actors.query.filter(Actors.id == id).one_or_none()

    actor.name = "osama"
    actor.age = 100
    actor.gender = "Male"

    try: 
      actor.update()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "actor": actor.format(),
      "acrors": actors_lsit
    }),200

  @app.route('/actors/<int:id>', methods=['DELETE', 'GET'])
  def delete_actors(id):
    
    actor = Actors.query.filter(Actors.id == id).one_or_none()

    try: 
      actor.delete()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "actor": id,
    }),200


#  Movies
#  ----------------------------------------------------------------

  @app.route('/movies', methods=['GET'])
  def get_movies():
    
    movies = Movies.query.all()
    movies_list = [movie.format() for movie in movies]

    return jsonify({
      "success": True, 
      "movies": movies_list
    }),200


  @app.route('/movies/post', methods=['POST', 'GET'])
  def post_movies():
    
    movie = Movies(
      title = "aya",
      release_date = "25",
    )
    
    try:
      movie.insert()
    except:
      abort(422)
    
    movies = Movies.query.all()
    movies_lsit = [movie.format() for movie in movies]
    
    return jsonify({
      "success": True, 
      "actor": movie.format(),
      "actors": movies_lsit
    }),200


  @app.route('/movies/<int:id>/patch', methods=['PATCH', 'GET'])
  def edit_movies(id):
    
    movies = Movies.query.all()
    movies_lsit = [movie.format() for movie in movies]

    movie = Movies.query.filter(Movies.id == id).one_or_none()

    movie.title = "osama"
    movie.release_date = "22"

    try: 
      movie.update()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "actor": movie.format(),
      "acrors": movies_lsit
    }),200


  @app.route('/movies/<int:id>/delete', methods=['DELETE', 'GET'])
  def delete_movies(id):
    
    movie = Movies.query.filter(Movies.id == id).one_or_none()

    try: 
      movie.delete()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "actor": id,
    }),200

  

  return app

APP = create_app()
'''
# Default port:
if __name__ == '__main__':
    APP.run()

'''
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
