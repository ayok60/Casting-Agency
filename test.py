import os
import unittest
import json

from app import create_app
from models import setup_db, Movies, Actors, Castings

CASTING_ASSISTANT = (
                      'eyJhbGciOiJSUzI1NiIsInR5cCI6'
                      'IkpXVCIsImtpZCI6Ik5qQkNSa1'
                      'EzTmtSRlJVUXdNME00TXpjNVJr'
                      'TXlOelZCTTBORFJEUXlNVGsyU'
                      'XpKQ1JrTXlRdyJ9.eyJpc3MiOiJodHRwczovL'
                      '2VzYWdlLmF1dGgwLmNvbS8'
                      'iLCJzdWIiOiJhdXRoMHw1ZT'
                      'IyMjI4NWY4MjhmYzBlOTM5'
                      'ZWEyMTEiLCJhdWQiOiJjYX'
                      'N0aW5nLWFnZW5jeSIsImlhdCI6MT'
                      'U3OTUxMzk3OSwiZXhwIjoxNTc5NjAw'
                      'Mzc5LCJhenAiOiJ0S0lIT0NpVkVzTUQ'
                      'wYVZ1eUZ6WW1VU3BVUzFCV2hyeSIsInNj'
                      'b3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ'
                      '2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0'
                      '.dWp9RxbudYBH4dOVGEBZhGJOQFF4XwS7'
                      'DsBBFNmrF6dpCK4B-CEnJpV1JLVG8UMTb'
                      'NJP_VtsraMhshwWVwb8godKroue4pgCr'
                      'BsI8V5Q3cSHQ-8FhnpOTf0_te6ydoBy78u'
                      'O9dQCYtA7i2A32QW9OU7MTV9m9iCj70-kt'
                      'lhpYweP5SGMxyK8hfoNSXD9a1rKDAEvP4u'
                      'Y57eI-TQaHg-4odEZhACy78LBdeRADbu0O'
                      '6bfkxa27sJTBq3cVLbyscVJRr-TrJpcqh42v'
                      'v9SJRoDo1RRtnNeggmybg_UB_C2weK7HezvbsJA'
                      '-v6Dz49pMY7v29Oj_QRLo5-2bD2M5cM-jw'
                    )


CASTING_DIRECTOR = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC'
                    'IsImtpZCI6Ik5qQkNSa1EzTmtSRlJVUXdNM'
                    'E00TXpjNVJrTXlOelZCTTBORFJEUXlNVGs'
                    'yUXpKQ1JrTXlRdyJ9.eyJpc3MiO'
                    'iJodHRwczovL2VzYWdlLmF1dGgw'
                    'LmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTIxZGExNWVmM'
                    'zkzNDBkY2QxYzczOWQiLCJhdWQiOiJjYXN0aW5nLWFnZW'
                    '5jeSIsImlhdCI6MTU3OTUxNDAxNCwiZXhwIjoxNTc5NjAwND'
                    'E0LCJhenAiOiJ0S0lIT0NpVkVzTUQwYVZ1eUZ6WW1VU3BVUzF'
                    'CV2hyeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVs'
                    'ZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzI'
                    'iwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdD'
                    'phY3RvcnMiXX0.N93SmGsmSyZlJe_XjKxtYi'
                    'xj9O3HDBfXQcnUisNCme8e6OK2v'
                    '_mz1Ws2xaSL_GXhuFIAfgciVXphOkIBxGDAN6Hr33CTzBFEjlG'
                    'lMLodhbGehGM2WsNIb3-kKLQx4pqb-vtdpzIt7ECjdEIGoQM1os'
                    'j_0bbu1aD6iXPHl3rqh9Tgzv3cHOi_uvWAcaX2uzYan5jtq'
                    '7k5-0YoDJ2Ygd3M5N5XS-K9UUt1s66M647nWohL-b20RG9RLq-v60Y2'
                    '2MjZJ2l3HLKR05SL1EhzpyH5qPz0idFxZaU-BkpriUvSSKYAMRep3gj'
                    'ZsMXYp3BVONZ-DF22U-KqEF-0aIMSNswrfw'
                    )

EXECUTIVE_PRODUCER = (
                    'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXV'
                    'CIsImtpZCI6Ik5qQkNSa1EzTmtSRl'
                    'JVUXdNME00TXpjNVJrTXlOelZCTTBOR'
                    'FJEUXlNVGsyUXpKQ1JrTXlRdyJ9.eyJpc'
                    '3MiOiJodHRwczovL2VzYWdlLmF'
                    '1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUt'
                    'b2F1dGgyfDEwMjc4NzYxODkzNDU0NDQ3NTgxNyIs'
                    'ImF1ZCI6WyJjYXN0aW5nLWFnZW5jeSIsImh0dHBz'
                    'Oi8vZXNhZ2UuYXV0aDAuY29tL3VzZXJpbmZvIl0sI'
                    'mlhdCI6MTU3OTUxMzkwOSwiZXhwIjoxNTc5NjAwMz'
                    'A5LCJhenAiOiJ0S0lIT0NpVkVzTUQwYVZ1eUZ6WW1VU'
                    '3BVUzFCV2hyeSIsInNjb3BlIjoib3BlbmlkIHByb2Zpb'
                    'GUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y'
                    'WN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3Rvcn'
                    'MiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0'
                    'Y2g6bW92aWVzIiwicG9zdDphY3Rvcn'
                    'MiLCJwb3N0Om1vdmllcyJdfQ.Ki2Dxc9aTHmlrAIOG0XOsUI'
                    'S0CypvD3CG7JoxF3i6w_3g'
                    't4LyDow0zbnrdyIqoozF5pjspVG6slfgsU1Urff-MOOjK5Pd'
                    'bczB-qAUIKRQvI5X6PrfAYizriiFHGIYfYqGVXbI_e_urrwcp'
                    'VQZhybRQaCUOXnmIAI3Smx7i7YgOsp1dMQXnzLJD6NMEZCNd'
                    'Aspl7aP4vW66ULObI8JWhLrnoe7kHc6uRrogJ0gV1gUfEiU0'
                    'eG6tvs_xTFFeXYKJyVtNczwIe5wCpLJOATV4Gu44eqZFHq'
                    'cRjPez_B-KAgswXBrCAjQq4-mY1U-Q89w2OKH-r'
                    'IAa7TXgI9tydaj9d0gQ'
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
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        res = client.get('/actors', headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['actors'])

    def test_add_actor(self):
        test_data = {
            'name': 'Test actor',
            'age': 20,
            'gender': 'Male',
            'image_link': '',
        }
        res = client.get('/actors', json = test_data,headers={'Authorization': f'Bearer {CASTING_ASSISTANT}'})

        

    def 

    



if __name__ == "__main__":
unittest.main()