from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.create_product, name='create_product'),
    path('inventories/product/<int:product_id>/', views.update_product_stock, name='update_product_stock'),
    path('orders/', views.create_order, name='create_order'),

    path('list/', views.list_products, name='list_products'),
]
