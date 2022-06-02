from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from blog.models import Article 

# Create your tests here.
class TestSArticle (TestCase):
    def setUp(self):
        self.client.login(username="raneem" , password="00000")

    def test_authentication_required(self):
        # self.client.logout()
        
        url = reverse('article_list')
        
        response =self.client.get(url)
        self.assertEqual (response.status_code ,status.HTTP_403_FORBIDDEN)


class ArticleTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testarticle = Article.objects.create(title = "test_article", content="Testing article")
        testarticle.save()


    def test_books_model(self):
        article = Article.objects.get(id=1)
        actual_title = article.title
        actual_content = article.content
        self.assertEqual(actual_title, "test_article")
        self.assertEqual(actual_content, "Testing article")
