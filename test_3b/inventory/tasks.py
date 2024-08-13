from celery import shared_task
from .models import Product


@shared_task
def check_stock_alert(product_id):
    try:
        product = Product.objects.get(pk=product_id)
        if product.stock < 10:
            print(f"Alerta: El stock del producto {product.name} es menor a 10.")
    except Product.DoesNotExist:
        print(f"El producto con ID {product_id} no existe.")