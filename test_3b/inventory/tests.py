from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Product

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(sku="sku_001", name="Agua")


    def test_update_stock(self):
        response = self.client.patch(f'/api/inventories/product/{self.product.id}/', {'stock': 9})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 9)


    def test_create_order(self):
        # Create a new product to place an order
        product = Product.objects.create(sku="sku_003", name="Lata", stock=10)
        response = self.client.post('/api/orders/', {'product_id': product.id, 'quantity': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.stock, 5)

