from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone

from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList
from .models import Category, Article


class UrlsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            category='Innovations',
            slug='innovations'
        )
        cls.article = Article.objects.create(
            title='Test Article',
            description='Test description',
            slug='test-article',
            pub_date=timezone.now(),
            main_page=True,
            category=cls.category
        )

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_articles_list_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url_resolves_articles_list_view(self):
        view = resolve('/articles')
        self.assertEqual(view.func.view_class, ArticleList)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('innovations',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url_resolves_category_view(self):
        view = resolve('/articles/category/innovations')
        self.assertEqual(view.func.view_class, ArticleCategoryList)

    def test_article_detail_status_code(self):
        url = self.article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url_resolves_article_detail_view(self):
        url = f"/articles/{self.article.pub_date.strftime('%Y')}/{self.article.pub_date.strftime('%m')}/{self.article.pub_date.strftime('%d')}/{self.article.slug}"
        view = resolve(url)
        self.assertEqual(view.func.view_class, ArticleDetail)
