from django.test import TestCase ,Client
from django.urls.base import reverse
from . . models import Recipes
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail',args=['some-recipe'])
        





    def test_recipe_list_GET(self):
        response = self.client.get(reverse('list'))
        self.assertEquals(response.status_code,200)