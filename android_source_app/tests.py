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

class TestEmailConfirmationFlow(BaseTestCase):
    def test(self):
        # Pretend someone filled out a form requesting the source for Linux
        # This would create a database column for their email address...
        self.requester = android_source_app.models.Requester.objects.create(
            email='linuxlover@example.com')

        # ...and for the actual request of source code.
        self.source_request = android_source_app.models.AndroidSourceRequest.objects.create(
            handset=self.g1,
            requester=self.requester,
            requester_name='Linux Lover')

        # NOTE that the name of the person is logged in the specific SourceRequest
        # rather than in the Requester!

        # Test that source requests start as unconfirmed,
        # remain unconfirmed in the face of wrong confirmation keys,
        # and become confirmed in the face of right ones.
        self.assertFalse(self.source_request.request_is_confirmed)
        self.source_request.mark_confirmed(key='stupid_stuff')
        self.assertFalse(self.source_request.request_is_confirmed)

        key = self.source_request.get_email_confirmation_key()
        self.source_request.mark_confirmed(key=key)
        self.assertTrue(self.source_request.request_is_confirmed)
