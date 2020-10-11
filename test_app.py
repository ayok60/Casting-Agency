

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors


CASTING_ASSISTANT = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YzJjNDRkMjAyMDA2OTU0ZTcwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDY5ODgsImV4cCI6MTYwMjQ5MzM4OCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.oG2Ml5gojxZQ6LUvgNmI5R2fQK8xd8kEqlih27orUrWfrMayswkzK00yvXg8Htdvk2B1Z_yetx4Jjd2J0lsNOkE0kwI3G7G-PUst-pvst4pcyA0kXgXdNJKt4iEzGCc_9Ca2pIWFec2GT6unWUy2aJRWpq4QbF4Zoy3MsfbesZYj-ni_OKba4s7MRARLbIvpc32v5PBYkXp5SOnM6Z1T8FL7PVOD7EoZkPGqVNCuv2cHQ-sKWEuAVdb9OYkStcx3KzFVOBNM46okX4WhWDN6eUf4LuyhdDnvfdCp5B2qcx49eUlFfkTatZpp5t99XMZdyG7av4FgXDddav_JpFLK5Q'
                    )


CASTING_DIRECTOR = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YmU3M2I0YWRlMDA2YmZhNGMyOSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDcwNTYsImV4cCI6MTYwMjQ5MzQ1NiwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.eLYHbgKxKm85UMQMCdCv4rH5PF-1guz6UD9N3fAcSMymizZHdQMSIZov2dzEzTd_p_uBC53C3AqYWsfMVx8X-kOHySJmXjSdXUXHEzu0IkcV0MnIlM_c0qEsUMcuXyNrevE8NqOqkYJ1joECBbSbe7vBvciAi50oN1DSxZ5myYA-7uQl6pv6z1Ct8dPJTXrsNiLW8KqVeCmsTY1-MzRjdpHEB128iWjdsPw2kRsUOS62VpPLDTJZz9hiSEKGzW0vpme8yfOxzBU8qcFXbABgD7MPngOpcchaT2FnKS0C83AmQpxcrynTcRg280_Bu0v8ZRDm-YDAgX6eZSsccwnkxw'
                    )

EXECUTIVE_PRODUCER = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmUyYzEzNDRkMjAyMDA2OTU0ZDZmMyIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDI0MDY5MjUsImV4cCI6MTYwMjQ5MzMyNSwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.VUUbTRq3iucH_5TOckEXl_9OMhQ9VRmrJmLcfn2i41Lm0GhWaxhRoOLF-jAdjLsK6k3v8vhZSKNMYlbGt3pYYA2-mRIrGcMeSm62Kk7ktJpmJnWIHbGMbbhhcN-nXgKA5c7xZA6EpRIxQMAnXsccf_H-lyiTsjxoRWBJUZponCaFTQhjKzkzrdM0T_KZVrZka9lWarNC1wn2MfrQnAbOAwICjmgdHdS6mCfhwV06ibjhg0kqZfTM1-gr1K9TgNfvSVTJKLGvwuxychYlflFKLyh4Umx4kj6rsOdXyDyEJe0jvQ_MevXSORD9NxsD8eZqJtfq6d1KSFafM_jNL-76qA'
                    )



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