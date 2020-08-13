from django.test import TestCase

from . import models


class CategoryTestCase(TestCase):
    def test_categories(self):
        category = models.Category.objects.get(id=1)
        print(category)
        self.assertEqual(category.name, 'Commonly Used Blocks')

        block = models.Block.objects.get(id=1)
        print(block)
        self.assertEqual(block.name, 'LOGICAL_OP')

        for category in models.Category.objects.all().order_by('sort_order'):
            print(category.id, category.name, category.sort_order)
            for block in models.Block.objects.filter(categories=category.id).order_by('name'):
                print(block.name)
            print()
