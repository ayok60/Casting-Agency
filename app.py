import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Movies, Actors, Castings

from auth import AuthError, requires_auth


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

#  Actors
#  ----------------------------------------------------------------


  '''
  Get Actors
  '''
  @app.route('/actors', methods=['GET'])
  @requires_auth('view:actors')
  def get_actors(jwt):
    
    actors = Actors.query.all()

    if not actors:
      abort(404)

    actors_lsit = [actor.format() for actor in actors]
    
    return jsonify({
      "success": True, 
      "actors": actors_lsit
    }),200


  '''
  Add Actor
  '''
  @app.route('/actors', methods=['GET','POST'])
  @requires_auth('add:actor')
  def post_actors(jwt):
    
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


  '''
  Edit Actor
  '''
  @app.route('/actors/<int:id>', methods=['PATCH', 'GET'])
  @requires_auth('edit:actors')
  def edit_actors(jwt, *args, **kwargs):
    
    id = kwargs['id']

    if not id:
      abort(404)

    body = request.get_json()
    actor = Actors.query.filter(Actors.id == id).one_or_none()

    actors = Actors.query.all()
    actors_lsit = [actor.format() for actor in actors]

    if not actor:
        abort(404)

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


  '''
  Delete Actor
  '''
  @app.route('/actors/<int:id>', methods=['DELETE', 'GET'])
  @requires_auth('delete:actor')
  def delete_actors(jwt, *args, **kwargs):

    id = kwargs['id']

    if not id:
        abort(404)
    
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


  '''
  Get Movies
  '''
  @app.route('/movies', methods=['GET'])
  @requires_auth('view:movies')
  def get_movies(jwt):
    
    movies = Movies.query.all()

    if not movies:
        abort(404)

    movies_list = [movie.format() for movie in movies]

    return jsonify({
      "success": True, 
      "movies": movies_list
    }),200


  '''
  Add Movie
  '''
  @app.route('/movies', methods=['POST', 'GET'])
  @requires_auth('add:movie')
  def post_movies(jwt):

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


  '''
  Edit Movie
  '''
  @app.route('/movies/<int:id>', methods=['PATCH', 'GET'])
  @requires_auth('edit:movies')
  def edit_movies(jwt, *args, **kwargs):

    id = kwargs['id']

    if not id:
        abort(404)
    
    movies = Movies.query.all()
    movies_lsit = [movie.format() for movie in movies]

    movie = Movies.query.filter(Movies.id == id).one_or_none()

    body = request.get_json()
    
    if not movie:
        abort(404)

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


  '''
  Delete Movie
  '''
  @app.route('/movies/<int:id>', methods=['DELETE', 'GET'])
  @requires_auth('delete:movie')
  def delete_movies(jwt, *args, **kwargs):

    id = kwargs['id']

    if not id:
        abort(404)
    
    movie = Movies.query.filter(Movies.id == id).one_or_none()
    castings = Castings.query.filter(Castings.movie_id == id).all()
    castings_list = [casting.actor_id for casting in castings]

    try: 
      for casting in castings:
        casting.delete() 

      movie.delete()
      

    except:
      abort(422)
    
    return jsonify({
      "success": True, 
      "cast": castings_list,
      "movie": id,
    }),200


  '''
  Get Movie Cast
  '''
  @app.route('/castings/movies/<int:id>', methods=['GET'])
  @requires_auth('view:movies')
  def get_castings_actors(jwt, *args, **kwargs):

    id = kwargs['id']

    if not id:
        abort(404)

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

    
  '''
  Add Movie Cast
  '''
  @app.route('/castings/movies', methods=['POST','GET'])
  @requires_auth('edit:movies')
  def post_castings_actors(jwt):
    
    

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

  '''
  Remove Actor from Movie
  '''
  @app.route('/movies/<int:movie_id>/<int:actor_id>', methods=['DELETE','GET'])
  @requires_auth('edit:movies')
  def delete_castings_actors(jwt, *args, **kwargs):

    movie_id = kwargs['movie_id']
    actor_id = kwargs['actor_id']
    
    casting = Castings.query.filter_by(movie_id = movie_id, actor_id = actor_id ).first()


    casting.delete()
    
    return jsonify({
      "success": True, 
      "movie": movie_id,
      "actor": actor_id,
    }),200



  
    
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          'success': False,
          'error': 404,
          'message': 'resource not found'
  }),404


  def __init__(self, error, status_code):
          self.error = error
          self.status_code = status_code


  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
      response = jsonify(ex.error)
      response.status_code = ex.status_code
      return response

  return app

app = create_app()
'''
# Default port:
if __name__ == '__main__':
    APP.run()

'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
