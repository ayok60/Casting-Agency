

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movies, Actors, Castings


CASTING_ASSISTANT = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YzJjNDRkMjAyMDA2OTU0ZTcwMCIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc4MTQsImV4cCI6MTYwMjQzNDIxNCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.OK0AFcw1qSzCFiYvL5_7oD9maD6OigskWa8hhjTPhkP_7w0mpOxIh2FJ5UTV70rpjEtEI_4nUZVq9qC1U4WdYTdo99i_aHkY_M-NwKOVfkysh8rvq2T_qdN2f2y_Fv4eI8OFKtsHiaxT60CrPHjLVyumza2YyPf-opXsf8TnIo1AvFSLGvHlhyTgdxbLwS0KtILLwhN9niPHXYXeILsORDNhZi0z6P68laOZDh1NeYdDfl7O62lIaLyuVg6ppw9jxQIVFeF42vkVguqiLaEGUugVVSL1Fe-MGRzxDUdFQfXd1Qgmz7D5b3yKbmU5l4yw7W50AeLiY1omVEG82Un5Ug'
                    )


CASTING_DIRECTOR = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmU1YmU3M2I0YWRlMDA2YmZhNGMyOSIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc5NDAsImV4cCI6MTYwMjQzNDM0MCwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.WpkOZG5WWe89iiZpC4rdyxXy9v_WgNaiKDCgGF7Qmvn1ZBgjel4RKnlbHNd14jq9Ti4oM2vHTgSmLm2cRd8D4ift6cZ1iGVd5fYRW_SQufw5hkS0jXTFvyrJqhvNalIy-DjFjFzs1AZiegpoeA0n0hNr0Yf1xAOAGSdhZTgwAKJHAe3kgaqjoQEhmOn6a0bKix5THkgyZ38j-AkCBCaK_NhpOnSRwwbTLB8tHg7N-yTehcSPq1kcrTQqJBF6SOl2CkMD7Ok2PjuilIhfFPRwiqvjg6k80l9CySuoRUhB47nTMqzmC6_tuEkixHxMV0osQOC89nGuPqTumCbXWV3FDQ'
                    )

EXECUTIVE_PRODUCER = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxfRmxzc2o5UFFFMEdjQUNud2U3SyJ9.eyJpc3MiOiJodHRwczovL2Nhc3RpbmctYWdlbmN5LXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNmUyYzEzNDRkMjAyMDA2OTU0ZDZmMyIsImF1ZCI6ImNhc3RpbmciLCJpYXQiOjE2MDIzNDc4NzksImV4cCI6MTYwMjQzNDI3OSwiYXpwIjoicDhRNFRKZzRvNGFySUNDQ09tWTNvYjIwdTVBRFpSc1kiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.Fm_iZe-KXuVX2sN-GhzJrGk-Sp3FY2tF9aynJP_LOqDAh_6uBnzCbc1VHtJEud53GZSfn3ZZBTewQp94HeSA709s0SGXytW5N7-A-HBd55hiMuqCPFtb8qH7nq9y2noQLE1kVYHrrlbvB-NGYYkS1ppmCFleqdJyajFx_SyEB1sQUsdOBZZgiaGtJFQWTp7g9FZ0vksWH3koPCo3hVJNHoT7C7mtzcEPx6PvS5UBR1YzqTHJV-HqbSHlMUKFuQae5NTOqMZ2nJLUsUrsQsY5ej_uEuZXcp8ymWU3ZNvLjArrVvvMXMN2XoNsNkiUDGYEMaeinp_7MElHnnpkP-8f6Q'
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