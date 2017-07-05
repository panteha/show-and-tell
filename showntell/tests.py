from django.test import TestCase
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from showntell.views import home_page
# Create your tests here.
class SmokeTest(TestCase):
    def test_unit_tests_work(self):
        self.assertEquals(1,1)
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>ShowNTell</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
