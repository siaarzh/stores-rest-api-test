from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/Books')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('Books'))
                self.assertDictEqual({'id': 1, 'name': 'Books', 'items': []},
                                     json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                response = client.post('/store/Books')

                self.assertEqual(response.status_code, 400)

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                response = client.delete('/store/Books')

                self.assertEqual(response.status_code, 200)
                self.assertIsNone(StoreModel.find_by_name('Books'))
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(response.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                response = client.get('/store/Books')

                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(StoreModel.find_by_name('Books'))
                self.assertDictEqual({'id': 1, 'name': 'Books', 'items': []},
                                     json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                response = client.get('/store/Books')

                self.assertEqual(response.status_code, 404)
                self.assertIsNone(StoreModel.find_by_name('Books'))
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                response = client.get('/store/Books')

                self.assertEqual(response.status_code, 200)
                self.assertIsNotNone(StoreModel.find_by_name('Books'))
                self.assertDictEqual({'id': 1, 'name': 'Books', 'items': [
                    {
                        'name': 'Alice',
                        'price': 19.99
                    }
                ]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                StoreModel('Bikes').save_to_db()
                response = client.get('/stores')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({
                    'stores': [
                        {
                            'id': 1,
                            'name': 'Books',
                            'items': []
                        },
                        {
                            'id': 2,
                            'name': 'Bikes',
                            'items': []
                        }
                    ]
                },
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Books').save_to_db()
                StoreModel('Bikes').save_to_db()
                ItemModel('Alice', 19.99, 1).save_to_db()
                ItemModel('Bianci', 2019.99, 2).save_to_db()
                response = client.get('/stores')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({
                    'stores': [
                        {
                            'id': 1,
                            'name': 'Books',
                            'items': [
                                {
                                    'name': 'Alice',
                                    'price': 19.99
                                }
                            ]
                        },
                        {
                            'id': 2,
                            'name': 'Bikes',
                            'items': [
                                {
                                    'name': 'Bianci',
                                    'price': 2019.99
                                }
                            ]
                        }
                    ]
                },
                                     json.loads(response.data))
