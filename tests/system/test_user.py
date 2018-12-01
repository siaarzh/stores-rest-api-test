from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:  # allows method to act as ext. client
            with self.app_context():
                request = client.post('/register', data={
                    'username': 'test',
                    'password': '1234'
                })

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(request.data))

    def test_register_and_login(self):
        pass

    def test_register_duplicate_user(self):
        pass