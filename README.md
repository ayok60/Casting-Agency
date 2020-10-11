
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
                   'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YzJjNDRkMjAyMDA2OTU0ZTcwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc4MTQsImV4cCI6MTYwMjQzNDIxNCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.OK0AFcw1qSzCFiYvL5_7oD9maD6OigskWa8hhjTPhkP_7w0mpOxIh2FJ5UTV70rpjEtEI_4nUZVq9qC1U4WdYTdo99i_aHkY_M-NwKOVfkysh8rvq2T_qdN2f2y_Fv4eI8OFKtsHiaxT60CrPHjLVyumza2YyPf-opXsf8TnIo1AvFSLGvHlhyTgdxbLwS0KtILLwhN9niPHXYXeILsORDNhZi0z6P68laOZDh1NeYdDfl7O62lIaLyuVg6ppw9jxQIVFeF42vkVguqiLaEGUugVVSL1Fe-MGRzxDUdFQfXd1Qgmz7D5b3yKbmU5l4yw7W50AeLiY1omVEG82Un5Ug'
                 
> CASTING_DIRECTOR =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YmU3M2I0YWRlMDA2YmZhNGMyOSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc5NDAsImV4cCI6MTYwMjQzNDM0MCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.WpkOZG5WWe89iiZpC4rdyxXy9v_WgNaiKDCgGF7Qmvn1ZBgjel4RKnlbHNd14jq9Ti4oM2vHTgSmLm2cRd8D4ift6cZ1iGVd5fYRW_SQufw5hkS0jXTFvyrJqhvNalIy-DjFjFzs1AZiegpoeA0n0hNr0Yf1xAOAGSdhZTgwAKJHAe3kgaqjoQEhmOn6a0bKix5THkgyZ38j-AkCBCaK_NhpOnSRwwbTLB8tHg7N-yTehcSPq1kcrTQqJBF6SOl2CkMD7Ok2PjuilIhfFPRwiqvjg6k80l9CySuoRUhB47nTMqzmC6_tuEkixHxMV0osQOC89nGuPqTumCbXWV3FDQ'
                    
> EXECUTIVE_PRODUCER =
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmUyYzEzNDRkMjAyMDA2OTU0ZDZmMyIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc4NzksImV4cCI6MTYwMjQzNDI3OSwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.Fm_iZe-KXuVX2sN-GhzJrGk-Sp3FY2tF9aynJP_LOqDAh_6uBnzCbc1VHtJEud53GZSfn3ZZBTewQp94HeSA709s0SGXytW5N7-A-HBd55hiMuqCPFtb8qH7nq9y2noQLE1kVYHrrlbvB-NGYYkS1ppmCFleqdJyajFx_SyEB1sQUsdOBZZgiaGtJFQWTp7g9FZ0vksWH3koPCo3hVJNHoT7C7mtzcEPx6PvS5UBR1YzqTHJV-HqbSHlMUKFuQae5NTOqMZ2nJLUsUrsQsY5ej_uEuZXcp8ymWU3ZNvLjArrVvvMXMN2XoNsNkiUDGYEMaeinp_7MElHnnpkP-8f6Q'
                    


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
