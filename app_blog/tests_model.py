from django.test import TestCase
from django.utils import timezone

from .models import Category, Article


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(category='Innovations', slug='innovations')
        Article.objects.create(
            title='Test Title',
            description='Test Description',
            slug='test-title',
            pub_date=timezone.now(),
            main_page=True,
            category=category
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        expected_url = (
            f"/articles/{article.pub_date.strftime('%Y')}/"
            f"{article.pub_date.strftime('%m')}/"
            f"{article.pub_date.strftime('%d')}/"
            f"{article.slug}"
        )
        self.assertEqual(article.get_absolute_url(), expected_url)
