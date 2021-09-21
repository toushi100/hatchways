from django.test import SimpleTestCase
from django.urls import   resolve
from django.urls.base import reverse
from . . views import listRecipes,DetailRecipes

class TestUrls (SimpleTestCase):

    def test_list_url_is_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func,listRecipes)
    def test_detail_url_resolves(self):
        url = reverse('detail',args=['some recipe'])
        self.assertEquals(resolve(url).func.view_class,DetailRecipes)