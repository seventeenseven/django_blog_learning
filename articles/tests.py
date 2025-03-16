from django.test import TestCase
from django.urls import reverse
from .models import Categorie

# Create your tests here.
class ArticleTest(TestCase):
    def test_creation_categorie(self):
        obj_category = Categorie.objects.create(nom="Audio")
        self.assertIsInstance(obj_category, Categorie, 'Test categorie passé')
    
    def test_postdetail_reponse(self):
        #response = self.client.get(reverse('post_detail',kwargs={'type': 'article',
        #                                                         'id':20}))
        #self.assertEqual(response.status_code, 200)
        pass