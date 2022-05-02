from django.test import TestCase, Client
from django.urls import reverse, resolve

from .models import Links

class TestModels(TestCase):    
    def test_links_str(self):
        link = Links.objects.create(original_link='https://github.com/', short_link='https://tinyurl.com/4dyt6b')
        
        self.assertEqual(link.__str__(), 'https://tinyurl.com/4dyt6b')


class TestViews(TestCase):
    def setUp(self) -> None:
        self.cliente = Client()
        self.url = reverse('home')

    def test_urls_template(self):
        res = self.client.get(self.url)

        self.assertEqual(self.url, '/')
        self.assertEqual(resolve('/').view_name, 'home')
        self.assertTemplateUsed(res, 'home.html')
    
    def test_create_short_link(self):
        payload = {'link': 'https://www.google.com/'}

        res = self.client.post(self.url, payload)

        self.assertEqual(res.status_code, 200)
        self.assertFalse(res.context['exists'])
    
    def test_create_short_link_exists(self):
        Links.objects.create(original_link='https://github.com/', short_link='https://tinyurl.com/4dyt6b')
        payload = {'link': 'https://github.com/'}

        res = self.client.post(self.url, payload)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.context['exists'])

