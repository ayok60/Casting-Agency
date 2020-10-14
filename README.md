
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
                   'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YzJjNDRkMjAyMDA2OTU0ZTcwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI2OTgyMTMsImV4cCI6MTYwMjc4NDYxMywiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.v3SSuQmFSDlylKCvRn5GDZVG6Ydoim8MOYlEdKlujH0MiRv32g7FsrrLclQ8CtnOQx-WrGpg2efHOQ9k0118rAgP9MrufMOZDtO5xKAiP3dmwIlRLEq3nvlpYsSchia8HQ8Wab58COKsUGoReW3RBf196xUL_Uac5Yn92uR1-Fqqtd2SUKo4WXnpc2EjrtDqeAeLGPnFDgQmAjpnvcoUyc95fNGQFs4n-MP2h5w6UBTr0MEogKI3dPdrsgPoBizeo7eUKWBLcY77lZ9hd79ggzW09E_1YQYq9PQo2tD_ZO5SWR5t03__T9zFO06ey1F31a-BZjGr9vMAsdlE6ybwFw'
                 
> CASTING_DIRECTOR =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YmU3M2I0YWRlMDA2YmZhNGMyOSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI2OTgxMjYsImV4cCI6MTYwMjc4NDUyNiwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.moFK3vknvtvuY8Cmu7EMQuAG_rsZjrF_P7qGAZeuy3qhm-oQEAgBXGWO_h5siqxQxKt2Ro7UrqTxrNZbSXdxWTK_NUiskr8ulxcCufm7qD7bX-t0Ssx62hqxjjpJ8tUi2FsUf_MGN4lzgmWbgJCkbsI-gIWLIfNR3fYqy6x72mfWEnHXv2Vrj8JJD66LRMyG2rVQBdEtH4UCcG_5kcimeav8b4UcWKN9OBvp7RVLm_VYbvwp5wzQTochDoZCr0f43P4ubgFPi25IKVN4qfob5Ej6Z96y3KVaDh27Z5oCC3-vgO1bdLLGHZjN2ffQPpKjvIX_lwMTyjI7wLlUy-tYag'
                    
> EXECUTIVE_PRODUCER =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmUyYzEzNDRkMjAyMDA2OTU0ZDZmMyIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI2OTgwMjAsImV4cCI6MTYwMjc4NDQyMCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.BgOMn6hujCVtXZfzAyhzjkqI9eM3nSJgWlnB_s-VYjx_RpYeFGd4_PDAqbViH4BSLkvE9YQYRWumHBBfD55nq3RciS-7nkLOuiLCFz3_Li-O27OYLmoqDa2lfqObDQqHx-2gNmS4xRz-wGPo7R6VGTpNUVxteGNQkyCeLGZGYgd57h_VGc48h0xxpgvgMHcOzZ9FrDWIbIdw6jmUhhbnODwN-DKzNMTaFk6X1WfsQgRZCPCXOCBsKOPEUhk46yPCv0Z_aHrexTidxtry2bdY9padfh0xETlxsdJ7JNu8VOYOgfNUyFNAYci1aXDrlOX8WzorzhsGLgIDVWm4xz6wKg'
                    


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
