import unittest
from flask import Flask
from flask import request, redirect, url_for
from app import app
from io import BytesIO

class MyTest(unittest.TestCase):

    def create_app(self):
        app = FLASK(__name__)
        app.config['TESTING'] = True
        return app

    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello')
        self.assertEqual(response.status_code, 200)
        assert 'Hello World!' in response.data

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        assert 'Upload new File' in response.data

    def test_image_upload(self):
        tester = app.test_client(self)
        tester.get('/')
	with open('images/orange.jpg') as fp:
            response = tester.post(data=dict(file=(fp, 'orange.jpg')), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = tester.get('/images/uploads/orange.jpg')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
