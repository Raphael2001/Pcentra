from django.test import TestCase, SimpleTestCase, Client
from .models import Shortener


# Create your tests here.

class CreateTest(TestCase):

    @classmethod
    def setUp(self):
        Shortener.objects.create(long_url="https://google.com")

    def test_create(self):
        # check if the long url is equal to the main url
        shortener = Shortener.objects.get(id=1)
        long_url = shortener.long_url
        self.assertEqual(long_url, "https://google.com")

    def test_redirect(self):
        # checking if the redirecting is working
        shortener = Shortener.objects.get(id=1)

        response = self.client.get(f'http://127.0.0.1:8000/{shortener.short_url}')
        self.assertEqual(response.url, "https://google.com")

    def test_non_existed(self):
        # checking if it returns 404 when a non exiting url is given
        response = self.client.get(f'http://127.0.0.1:8000/ggg')
        self.assertEqual(response.status_code,404)