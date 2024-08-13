# from django.test import TestCase
# from .models import Product

# class ProductTestCase(TestCase):
#     def setUp(self):
#         Product.objects.create(sku="sku_001", name="Agua")

#     def test_product_creation(self):
#         product = Product.objects.get(sku="sku_001")
#         self.assertEqual(product.name, "Agua")
#         self.assertEqual(product.stock, 100)

#     def test_update_stock(self):
#         product = Product.objects.get(sku="sku_001")
#         product.stock += 15
#         product.save()
#         self.assertEqual(product.stock, 120)
