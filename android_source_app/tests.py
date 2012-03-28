from django.utils import unittest
import django.test.client

class FrontPageTestCase(unittest.TestCase):
    def setUp(self):
        self.client = django.test.client.Client()

    def test_front_page_loads(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


