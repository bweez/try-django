from django.test import TestCase
from django.utils.text import slugify
from .models import Article
# Create your tests here.
from .utils import slugify_instance_title


class ArticleModelTestCase(TestCase):

    def setUp(self):
        self.test_title = 'Hello World'
        for i in range(0, 5):
            Article.objects.create(title=self.test_title,
                                   content='test content')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_slug(self):
        article = Article.objects.all().first()
        slugified_title = slugify(article.title)
        self.assertEqual(article.slug, slugified_title)

    def test_unique_slug(self):
        slugified_title = slugify(self.test_title)
        qs = Article.objects.exclude(slug=slugified_title)
        for article in qs:
            slugified_title = slugify(article.title)
            self.assertNotEqual(article.slug, slugified_title)

    # This is an example test from the Try Django course.  I dislike the original implementation
    # of the slugify function, it uses a pseudo-rand function with a small param range of 200k
    
    # def test_slugify_instance_title(self):
    #     article = Article.objects.all().first()
    #     new_slugs = []

    #     for i in range(0, 5):
    #         instance = slugify_instance_title(article, save=False)
    #         new_slugs.append(instance.slug)
    #     unique_slugs = list(set(new_slugs))
    #     self.assertEqual(len(unique_slugs), len(new_slugs))
