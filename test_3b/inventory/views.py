from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer, ProductStockUpdateSerializer


# Create your views here.

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_product_stock(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductStockUpdateSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if product.stock < 10:
            print(f"Alerta: El stock del producto {product.name} es menor a 10.")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    product_id = request.data.get('product_id')
    # quantity = request.data.get('quantity', 1)
    try:
        quantity = int(request.data.get('quantity', 1))  # Convierte quantity a entero
    except ValueError:
        return Response({'error': 'La cantidad debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if product.stock < quantity:
        return Response({'error': 'Stock insuficiente'}, status=status.HTTP_400_BAD_REQUEST)

    product.stock -= quantity
    product.save()

    if product.stock < 10:
        print(f"Alerta: El stock del producto {product.name} es menor a 10.")

    return Response({'message': 'Orden creada exitosamente'}, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data) 