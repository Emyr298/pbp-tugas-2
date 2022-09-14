from decimal import DivisionByZero
from django.test import TestCase
from katalog.models import CatalogItem
from django.core.exceptions import ObjectDoesNotExist

# References: https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises

# Create your tests here.
class CatalogItemTestCase(TestCase):
    def test_created_objects_exists(self):
        """Created objects exists in the database after create method"""
        CatalogItem.objects.create(
            item_name='Figur Animek',
            item_price=10000,
            item_stock=5,
            description='Figur animek bagi penyuka anime',
            rating=9,
            item_url='https://bad-smile.co.mltv/products/412542',
        )
        CatalogItem.objects.create(
            item_name='Mobil Mainan',
            item_price=2000,
            item_stock=5,
            description='Mobil mainan yang bisa di ngeng ngeng ngeng in',
            rating=6,
            item_url='https://bad-smile.co.mltv/products/12342',
        )
        try:
            CatalogItem.objects.get(item_name='Figur Animeks')
            CatalogItem.objects.get(item_name='Mobil Mainan')
        except CatalogItem.DoesNotExist:
            self.fail('Created item doesn\'t exists')
