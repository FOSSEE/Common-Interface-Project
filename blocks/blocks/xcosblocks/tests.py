from django.test import TestCase

from .models import Category, Block, BlockPort


PRINT_BLOCKS = False
PRINT_PORTS = False


class CategoryTestCase(TestCase):
    def test_categories(self):
        category = Category.objects.get(id=1)
        print(category)
        self.assertEqual(str(category), '4xxx')
        print()

        block = Block.objects.get(id=66)
        print(block)
        self.assertEqual(str(block), 'Buzzer')
        if PRINT_PORTS:
            blockports = block.blockport_set.all()
            for blockport in blockports:
                print(blockport)
        print()

        blockport = BlockPort.objects.get(id=88)
        print(blockport)
        self.assertEqual(str(blockport), '4011 2')
        print()

        categories = Category.objects.all().order_by('sort_order')
        allblocks = Block.objects.all() \
                .order_by('name')
        for category in categories:
            blocks = allblocks.filter(categories=category)
            print(category.id, category, len(blocks))
            if PRINT_BLOCKS:
                for block in blocks:
                    print(block)
                print()
        if not PRINT_BLOCKS:
            print()

        namestring = 'A'
        allblocks = Block.objects.filter(name__istartswith=namestring)
        categories = Category.objects.filter(block__in=allblocks).distinct()  \
            .order_by('sort_order')
        for category in categories:
            blocks = allblocks.filter(categories=category) \
                .order_by('name')
            print(category.id, category, len(blocks))
            if PRINT_BLOCKS:
                for block in blocks:
                    print(block)
                print()
        if not PRINT_BLOCKS:
            print()
