
# Casting Agency

Hosted on Heroku : https://casting-agency-project-udacity.herokuapp.com/Actors

## Description

Final Udacity Backend Web Developer Nanodegree program. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies this project aim to create a system to simplify and streamline this process.

## Dependencies

**Python 3.7**

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
$ export FLASK_APP=app
$ export FLASK_ENV=development
$ flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## API Reference

### Getting Started

**Base URL**

this application is hosted on Heroku https://casting-agency-project-udacity.herokuapp.com/Actors 

**Authentication**

Auth0 was used for implementing the authentication, by using RBAC to assign permissions for each role. The tokens below can be used for accessing the endpoints.

To setup your Auth0 in `auth.py`
```bash
AUTH0_DOMAIN = '<your auth domain>'
ALGORITHMS = ['RS256']
API_AUDIENCE = '<your api audience>'
```

The Auth0 tokens for each role (vaild only for 24 hours)

> CASTING_ASSISTANT =
                   'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YzJjNDRkMjAyMDA2OTU0ZTcwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDY5ODgsImV4cCI6MTYwMjQ5MzM4OCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.oG2Ml5gojxZQ6LUvgNmI5R2fQK8xd8kEqlih27orUrWfrMayswkzK00yvXg8Htdvk2B1Z_yetx4Jjd2J0lsNOkE0kwI3G7G-PUst-pvst4pcyA0kXgXdNJKt4iEzGCc_9Ca2pIWFec2GT6unWUy2aJRWpq4QbF4Zoy3MsfbesZYj-ni_OKba4s7MRARLbIvpc32v5PBYkXp5SOnM6Z1T8FL7PVOD7EoZkPGqVNCuv2cHQ-sKWEuAVdb9OYkStcx3KzFVOBNM46okX4WhWDN6eUf4LuyhdDnvfdCp5B2qcx49eUlFfkTatZpp5t99XMZdyG7av4FgXDddav_JpFLK5Q'
                 
> CASTING_DIRECTOR =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YmU3M2I0YWRlMDA2YmZhNGMyOSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDcwNTYsImV4cCI6MTYwMjQ5MzQ1NiwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.eLYHbgKxKm85UMQMCdCv4rH5PF-1guz6UD9N3fAcSMymizZHdQMSIZov2dzEzTd_p_uBC53C3AqYWsfMVx8X-kOHySJmXjSdXUXHEzu0IkcV0MnIlM_c0qEsUMcuXyNrevE8NqOqkYJ1joECBbSbe7vBvciAi50oN1DSxZ5myYA-7uQl6pv6z1Ct8dPJTXrsNiLW8KqVeCmsTY1-MzRjdpHEB128iWjdsPw2kRsUOS62VpPLDTJZz9hiSEKGzW0vpme8yfOxzBU8qcFXbABgD7MPngOpcchaT2FnKS0C83AmQpxcrynTcRg280_Bu0v8ZRDm-YDAgX6eZSsccwnkxw'
                    
> EXECUTIVE_PRODUCER =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmUyYzEzNDRkMjAyMDA2OTU0ZDZmMyIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDY5MjUsImV4cCI6MTYwMjQ5MzMyNSwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.VUUbTRq3iucH_5TOckEXl_9OMhQ9VRmrJmLcfn2i41Lm0GhWaxhRoOLF-jAdjLsK6k3v8vhZSKNMYlbGt3pYYA2-mRIrGcMeSm62Kk7ktJpmJnWIHbGMbbhhcN-nXgKA5c7xZA6EpRIxQMAnXsccf_H-lyiTsjxoRWBJUZponCaFTQhjKzkzrdM0T_KZVrZka9lWarNC1wn2MfrQnAbOAwICjmgdHdS6mCfhwV06ibjhg0kqZfTM1-gr1K9TgNfvSVTJKLGvwuxychYlflFKLyh4Umx4kj6rsOdXyDyEJe0jvQ_MevXSORD9NxsD8eZqJtfq6d1KSFafM_jNL-76qA'
                    


### Error Handling

Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 422,
    "message": "unprocessable"
}
```

Errors due to unauthorized access 
```
{
    "code": "unauthorized",
    "description": "Permissions not found."
}
```

The API will return three types of errors when unsuccessful request occur:

- 404: resource not found
- 422: unprocessable
- 401: unauthorized 

### Endpoints 

#### GET `/actors`

- General: 
  - Returns a list of actors, success value.
  - Can be accssed by Casting Assistant, Casting Director and Executive Producer
- Sample: 
```
  curl --request GET \
  --url http://127.0.0.1:5000/actors \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header 'content-type: application/json'
```

Return

```
  {
    "actors": [
      {
        "age": "41", 
        "gender": "Male", 
        "id": 1, 
        "image_link": null, 
        "name": "Kevin Heart"
      }
    ], 
    "success": true
  }
```

#### POST `/actors`

- General: 
  - create new actor by submiting the actor name, age, gender, and image link.
  - Returns a list of actors, success value.
  - Can be created only by Casting Director and Executive Producer
- Sample: 
```
  curl --request POST \
  --url http://127.0.0.1:5000/actors \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json" \
  --data '{"name": "Chris Evans", "age": 39, "gender": "Male"}'
```

Return

```
  {
    "actor": {
      "age": "39", 
      "gender": "Male", 
      "id": 2, 
      "image_link": null, 
      "name": "Chris Evans"
    }, 
    "actors": [
      {
        "age": "41", 
        "gender": "Male", 
        "id": 1, 
        "image_link": null, 
        "name": "Kevin Heart"
      }, 
      {
        "age": "39", 
        "gender": "Male", 
        "id": 2, 
        "image_link": null, 
        "name": "Chris Evans"
      }
    ], 
    "success": true
  }
```

#### PATCH `/actors/<int:id>`

- General: 
  - Edit an actor by the id with submiting the actor name, age, gender, and/or image link.
  - Returns a list of actors, success value.
  - Can be created only by Casting Director and Executive Producer
- Sample: 
```
  curl --request PATCH \
  --url http://127.0.0.1:5000/actors/2 \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json" \
  --data '{"image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Chris_Evans_in_2019.jpg/440px-Chris_Evans_in_2019.jpg"}'
```

Return

```
  {
    "actors": [
      {
        "age": "41", 
        "gender": "Male", 
        "id": 1, 
        "image_link": null, 
        "name": "Kevin Heart"
      }, 
      {
        "age": "39", 
        "gender": "Male", 
        "id": 2, 
        "image_link": null, 
        "name": "Chris Evans"
      }
    ], 
    "actor": {
      "age": "39", 
      "gender": "Male", 
      "id": 2, 
      "image_link": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Chris_Evans_in_2019.jpg/440px-Chris_Evans_in_2019.jpg", 
      "name": "Chris Evans"
    }, 
    "success": true
  }
```

#### DELETE `/actors/<int:id>`

- General: 
  - Delete an actor by the id.
  - Returns a list of actors, success value.
  - Can be created only by Casting Director and Executive Producer
- Sample: 
```
  curl --request DELETE \
  --url http://127.0.0.1:5000/actors/2 \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json"
```

Return

```
  {
    "actor": 2, 
    "success": true
  }
```

#### GET `/movies`

- General: 
  - Returns a list of movies, success value.
  - Can be accssed by Casting Assistant, Casting Director and Executive Producer
- Sample: 
```
  curl --request GET \
  --url http://127.0.0.1:5000/movies \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header 'content-type: application/json’

```

Return

```
  {
    "movies": [
      {
        "id": 1, 
        "image_link": null, 
        "release_date": "21/1/2019", 
        "title": "Jumanji: The Next Level"
      }, 
      {
        "id": 2, 
        "image_link": null, 
        "release_date": "14/2/2020", 
        "title": "Sonic the Hedgehog"
      }
    ], 
    "success": true
  }
```

#### POST `/movies`

- General: 
  - create new movie by submiting the movie title, release date and image link.
  - Returns a list of movies, success value.
  - Can be created only by Executive Producer
- Sample: 
```
  curl --request POST \
  --url http://127.0.0.1:5000/movies \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json" \
  --data '{"title": "The Angry Birds Movie", "release_date": "20/5/2016"}' 
```

Return

```
  {
    "movie": {
      "id": 3, 
      "image_link": null, 
      "release_date": "20/5/2016", 
      "title": "The Angry Birds Movie"
    }, 
    "movies": [
      {
        "id": 1, 
        "image_link": null, 
        "release_date": "21/1/2019", 
        "title": "Jumanji: The Next Level"
      }, 
      {
        "id": 2, 
        "image_link": null, 
        "release_date": "14/2/2020", 
        "title": "Sonic the Hedgehog"
      }, 
      {
        "id": 3, 
        "image_link": null, 
        "release_date": "20/5/2016", 
        "title": "The Angry Birds Movie"
      }
    ], 
    "success": true
  }

```

#### PATCH `/movies/<int:id>`

- General: 
  - Edit a movie by submiting the movie title, release date and/or image link.
  - Returns a list of movies, success value.
  - Can be created only by Casting Director and Executive Producer
- Sample: 
```
  curl --request PATCH \
  --url http://127.0.0.1:5000/movies/3 \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json" \
  --data '{"image_link": "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png"}'
```

Return

```
  {
    "movies": [
      {
        "id": 1, 
        "image_link": null, 
        "release_date": "21/1/2019", 
        "title": "Jumanji: The Next Level"
      }, 
      {
        "id": 2, 
        "image_link": null, 
        "release_date": "14/2/2020", 
        "title": "Sonic the Hedgehog"
      }, 
      {
        "id": 3, 
        "image_link": null, 
        "release_date": "20/5/2016", 
        "title": "The Angry Birds Movie"
      }
    ], 
    "movie": {
      "id": 3, 
      "image_link": "https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png", 
      "release_date": "20/5/2016", 
      "title": "The Angry Birds Movie"
    }, 
    "success": true
  }
```
#### DELETE `/movies/<int:id>`

- General: 
  - Delete a movie by the id.
  - Returns a list of movies, success value.
  - Can be created only by Executive Producer
- Sample: 
```
  curl --request DELETE \
  --url http://127.0.0.1:5000/movies/3 \
  --header "authorization: Bearer <YOUR_TOKEN>" \
  --header "content-type: application/json"
```

Return

```
  {
    "movie": 3, 
    "success": true
  }
```

## Author

The API was built `app.py` and tested `test_app.py` by Aya Khashoggi 
The idea of the app was done by [Udacity](https://www.udacity.com) as final project for [Full Stack Web Developer Nanodgree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)
