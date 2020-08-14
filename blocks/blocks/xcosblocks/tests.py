from django.test import TestCase

from .models import Category, Block


class CategoryTestCase(TestCase):
    def test_categories(self):
        category = Category.objects.get(id=1)
        print(category)
        self.assertEqual(category.name, 'Commonly Used Blocks')
        print()

        block = Block.objects.get(id=1)
        print(block)
        self.assertEqual(block.name, 'LOGICAL_OP')
        print()

        categories = Category.objects.all().order_by('sort_order')
        for category in categories:
            blocks = Block.objects.filter(categories=category) \
                .order_by('name')
            print(category.id, category.name, len(blocks))
            for block in blocks:
                print(block.name)
            print()

        namestring = 'A'
        blocks = Block.objects.filter(name__istartswith=namestring)
        categories = Category.objects.filter(block__in=blocks).distinct()  \
            .order_by('sort_order')
        for category in categories:
            blocks = Block.objects.filter(categories=category,
                                          name__istartswith=namestring) \
                .order_by('name')
            print(category.id, category.name, len(blocks))
            for block in blocks:
                print(block.name)
            print()
