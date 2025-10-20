from django.test import TestCase
from django.urls import reverse


class PingTest(TestCase):
    def test_ping(self):
        url = reverse('ping')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {'ping': 'pong'})
