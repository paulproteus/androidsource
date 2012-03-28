from django.utils import unittest
import android_source_app.models
import django.test.client

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = django.test.client.Client()
        self.factory = django.test.client.RequestFactory()
        self.htc = android_source_app.models.Manufacturer.objects.create(name="HTC")
        self.g1 = android_source_app.models.Handset.objects.create(
            name="G1",
            manufacturer=self.htc)

class FrontPageTestCase(BaseTestCase):
    def test_front_page_loads(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

