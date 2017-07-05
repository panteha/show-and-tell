import unittest
from flask import Flask
from flask import request, redirect, url_for
from flask_testing import TestCase
from app import app
from io import BytesIO

class MyTest(unittest.TestCase):

    def create_app(self):
        app = FLASK(__name__)
        app.config['TESTING'] = True
        return app

    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        assert 'Hello World!' in response.data

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        assert 'Upload new File' in response.data

    def test_image_upload(self):
        tester = app.test_client(self)
        tester.get('/', content_type='html/text')
        tester.post(data=dict(
                        file=(BytesIO(), 'goat.png'),
                    ), follow_redirects=True)
        response = tester.get('/images/uploads/goat.png', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
