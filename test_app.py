

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors


EXECUTIVE_PRODUCER = os.environ.get('EXECUTIVE_PRODUCER')
CASTING_DIRECTOR = os.environ.get('CASTING_DIRECTOR')
CASTING_ASSISTANT = os.environ.get('CASTING_ASSISTANT')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "db_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        #self.database_path = os.environ['TEST_DATABASE_URL']

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()
            
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    

    
    
    def test_add_actor(self):
        test_data = {
            'name': 'Test actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        res = self.client().post('/actors', json = test_data, headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,201)
        self.assertEqual(data['success'], True) 

    
        
    def test_422_add_actor(self):
        test_data = {
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }

        res = self.client().post(
            '/actors', 
            json = test_data,
            headers={'Authorization': f'Bearer {CASTING_DIRECTOR}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    def test_401_add_actor_unauthorized(self):
        test_data = {
            'name': 'Test actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        response = self.client().post(
            '/actors', 
            json = test_data,
            headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')


    def test_get_actors(self):
            res = self.client().get('/actors', headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'],True)
            self.assertTrue(data['actors'])


    def test_edit_actor(self):
        test_data = {
            'name': 'Test Patch actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        response = self.client().patch(
            '/actors/1',
            json = test_data,
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_edit_actor_unauthorized(self):
        test_data = {
            'name': 'Test Patch actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        response = self.client().patch(
            '/actors/1',
            json = test_data,
            headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')

    def test_404_edit_actor(self):
        test_data = {
            'name': 'Test Patch actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        response = self.client().patch(
            '/actor/9999',
            json=test_data,
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


    def test_401_delete_actor(self):
        response = self.client().delete(
            '/actors/1',
            headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')
    

    def test_404_delete_actor(self):
        response = self.client().delete(
            '/actors/9999',
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


    def test_delete_actor(self):
            response = self.client().delete(
                '/actors/1',
                headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
            )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['message'])


    

    def test_add_movie(self):
        test_data = {
            'title': 'Test movie',
            'release_date': '6.10.2020',
            'image_link': '',
        }
        res = self.client().post(
            '/movies', 
            json = test_data,
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,201)
        self.assertEqual(data['success'], True) 

    def test_401_add_movie_unauthorized(self):
        test_data = {
            'title': 'Test movie',
            'release_date': '6.10.2020',
            'image_link': '',
        }
        response = self.client().post(
            '/movies',
            json = test_data,
            headers={'Authorization': f'Bearer {CASTING_DIRECTOR}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')

    def test_get_movies(self):
            res = self.client().get('/movies', headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'],True)
            self.assertTrue(data['movies'])

    def test_edit_movie(self):
        test_data = {
            'title': 'Test patch movie',
            'release_date': '6.10.2019',
            'image_link': '',
        }
        response = self.client().patch(
            '/movies/1',
            json = test_data,
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_edit_movie_unauthorized(self):
        test_data = {
            'title': 'Test patch movie',
            'release_date': '6.10.2019',
            'image_link': '',
        }
        response = self.client().patch(
            '/movies/1',
            json = test_data,
            headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')

    def test_404_edit_moive(self):
        test_data = {
            'title': 'Test patch movie',
            'release_date': '6.10.2019',
            'image_link': '',
        }
        response = self.client().patch(
            '/movies/9999',
            json=test_data,
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')


    


    def test_401_delete_movie(self):
        response = self.client().delete(
            '/movies/1',
            headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'}
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permissions not found.')
    

    def test_404_delete_movies(self):
        response = self.client().delete(
            '/movies/9999',
            headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
        )

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['error'], 404)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_movie(self):
            response = self.client().delete(
                '/movies/1',
                headers={'Authorization': f'Bearer {EXECUTIVE_PRODUCER}'}
            )
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)

if __name__ == "__main__":
    unittest.main()