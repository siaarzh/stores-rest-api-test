from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        # get setUp() from BaseTest first
        super(ItemTest, self).setUp()
        # get access token prior to every test method
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({
                                               'username': 'test',
                                               'password': '1234'
                                           }),
                                           headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = 'JWT ' + auth_token

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/item/Alice')

                self.assertEqual(response.status_code, 401)  # no auth header

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                auth_header = {'Authorization': self.access_token}
                response = client.get('/item/Alice', headers=auth_header)

                self.assertEqual(response.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                auth_header = {'Authorization': self.access_token}
                response = client.get('/item/Alice', headers=auth_header)

                self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                response = client.delete('/item/Alice')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(response.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                response = client.post(
                    '/item/Alice',
                    data={
                        'price': 19.99,
                        'store_id': 1
                    }
                )

                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({'name': 'Alice', 'price': 19.99},
                                     json.loads(response.data))

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                response = client.post(
                    '/item/Alice',
                    data={
                        'price': 25.99,
                        'store_id': 1
                    }
                )

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': "An item with name 'Alice' already exists."},
                                     json.loads(response.data))

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                response = client.put(
                    '/item/Alice',
                    data={
                        'price': 19.99,
                        'store_id': 1
                    }
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('Alice').price, 19.99)
                self.assertDictEqual({'name': 'Alice', 'price': 19.99},
                                     json.loads(response.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()

                self.assertEqual(ItemModel.find_by_name('Alice').price, 19.99)

                response = client.put(
                    '/item/Alice',
                    data={
                        'price': 25.99,
                        'store_id': 1
                    }
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('Alice').price, 25.99)
                self.assertDictEqual({'name': 'Alice', 'price': 25.99},
                                     json.loads(response.data))

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                response = client.get('/items')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(
                    {
                        'items': [
                            {
                                'name': 'Alice',
                                'price': 19.99
                            }
                        ]
                    },
                    json.loads(response.data)
                )