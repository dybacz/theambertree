from django.test import TestCase
from menu import models
from django import shortcuts

class TestViews(TestCase):
    """"""

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


