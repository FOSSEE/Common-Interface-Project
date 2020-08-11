from django.test import TestCase

from . import models


class CategoryTestCase(TestCase):
    def setUp(self):
        models.Category.objects.create(name='ANDLOG', sort_order=30)

    def test_categories(self):
        category = models.Category.objects.get(name='ANDLOG')
        print(category)
        self.assertEqual(category.name, 'ANDLOG')
