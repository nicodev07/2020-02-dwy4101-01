from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
        )

        Article.objects.create(
            title="Retiro 10%",
            description = "Se viene el segundo retiro del 10%",
            views = 10,
            comments = 30,
            user = userCreate
        )

        Article.objects.create(
            title="Chile sale campeón de la Copa Confederaciones 2017",
            description = "Chile le gana 2-1 a Alemania en el último minuto.",
            views = 1000,
            comments = 300,
            user = userCreate
        )
    def test_count_views(self):
        retiro10 = Article.objects.get(title="Retiro 10%")
        self.assertEqual(retiro10.views, 10)

    def test_count_comments(self):
        retiro10 = Article.objects.get(title="Retiro 10%")
        self.assertEqual(retiro10.comments, 30)
    
    def test_add_comment(self):
        retiro10 = Article.objects.get(title="Retiro 10%")
        retiro10 = retiro10.addComment()
        self.assertEqual(retiro10.comments,31)

    def test_add_comments(self):
        retiro10 = Article.objects.get(title="Retiro 10%")
        retiro10 = retiro10.addComments(10)
        self.assertEqual(retiro10.comments,40)
