import unittest
from flask_testing import TestCase
from flask import Flask
from app import app  # import your Flask app

class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_add_item(self):
        # Use the test client to send a POST request to the add_item route
        response = self.client.post('/add_item', json={
            'title': 'Apple Network Card',
            'description': 'Apple Network Card',
            'price': 5.00,
            'cover': '/static/applenetworkcard-1.jpg',
            'images': ['/static/applenetworkcard-1.jpg'],
            'category': 'Electronics',
            'tags': [],
            'status': 'active',
            'owner': 'zn23'
        })

    # def test_remove_item(self):
    #     # Use the test client to send a DELETE request to the remove_item route
    #     response = self.client.delete('/remove_item/10')
    #     print(response.status_code)

    def test_save(self):
        # Use the test client to send a POST request to the add_user route
        response = self.client.get('/save')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
    