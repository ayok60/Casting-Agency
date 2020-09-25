import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movies, Actors, Castings

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
    
    body = request.get_json()
    
    actor = Actors(
      name = body.get('name'),
      age = body.get('age'),
      gender = body.get('gender'),
      image_link = body.get('image_link')
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

    body = request.get_json()

    actor.name = body.get('name') if body.get('name') else actor.name
    actor.age = body.get('age') if body.get('age') else actor.age
    actor.gender = body.get('gender') if body.get('gender') else actor.gender
    actor.image_link = body.get('image_link') if  body.get('image_link') else actor.image_link

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


  @app.route('/movies', methods=['POST', 'GET'])
  def post_movies():

    body = request.get_json()
    
    movie = Movies(
      title = body.get('title'),
      release_date = body.get('release_date'),
      image_link = body.get('image_link'),
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


  @app.route('/movies/<int:id>', methods=['PATCH', 'GET'])
  def edit_movies(id):
    
    movies = Movies.query.all()
    movies_lsit = [movie.format() for movie in movies]

    movie = Movies.query.filter(Movies.id == id).one_or_none()

    body = request.get_json()
    

    movie.title = body.get('title') if body.get('title') else movie.title
    movie.release_date = body.get('release_date') if  body.get('release_date') else movie.release_date
    movie.image_link = body.get('image_link') if  body.get('image_link') else movie.image_link
    
    print(movie.title)
    print(movie.release_date)

    try: 
      movie.update()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "movie": movie.format(),
      "acrors": movies_lsit
    }),200


  @app.route('/movies/<int:id>', methods=['DELETE', 'GET'])
  def delete_movies(id):
    
    movie = Movies.query.filter(Movies.id == id).one_or_none()
    castings = Castings.query.filter(Castings.movie_id == id).all()

    try: 
      movie.delete()
      castings.delete()

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "actor": id,
    }),200

  
  @app.route('/castings/movies/<int:id>', methods=['GET'])
  def get_castings_actors(id):
    
    

    castings = Castings.query.filter_by(movie_id = id).all()
    casting_lsit = [casting.format() for casting in castings]

    actors_list = [Actors.query.get(actor['actor_id']) for actor in casting_lsit]
    
    actors = []
    for actor in actors_list: 
      actors.append({
        'name' : actor.name,
        'id': actor.id
      })
    
    
    return jsonify({
      "success": True, 
      "castings": casting_lsit,
      "actors": actors,

    }),200

    

  @app.route('/castings/movies', methods=['POST','GET'])
  def post_castings_actors():
    
    

    body = request.get_json()

    castings = Castings(
      movie_id = body.get('movie_id'),
      actor_id = body.get('actor_id')
    )
    
    try:
      castings.insert()
    except:
      abort(422)
    

    
    return jsonify({
      "success": True, 
    }),200


  @app.route('/movies/<int:movie_id>/<int:actor_id>', methods=['DELETE','GET'])
  def delete_castings_actors(*args, **kwargs):

    movie_id = kwargs['movie_id']
    actor_id = kwargs['actor_id']
    
    casting = Castings.query.filter_by(movie_id = movie_id, actor_id = actor_id ).first()


    casting.delete()
    
    return jsonify({
      "success": True, 
      "movie": movie_id,
      "actor": actor_id,
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
