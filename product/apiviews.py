from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from .models import Product, Brand, Origin
from product.serializers import ProductSerializer, BrandSerializer, OriginSerializer, UserSerializer

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

class ProductList(APIView): 
    def get(self, request): 
        products = Product.objects.all()[:20]
        data = ProductSerializer(products, many=True).data 
        return Response(data)

class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk) 
        data = ProductSerializer(product).data 
        return Response(data)

class BrandList(APIView): 
    def get(self, request): 
        brands = Brand.objects.all()[:20]
        data = BrandSerializer(brands, many=True).data 
        return Response(data)

class BrandDetail(APIView):
    def get(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk) 
        data = BrandSerializer(brand).data 
        return Response(data)

class OriginList(APIView): 
    def get(self, request): 
        origins = Origin.objects.all()[:20]
        data = OriginSerializer(origins, many=True).data 
        return Response(data)

class OriginDetail(APIView):
    def get(self, request, pk):
        origin = get_object_or_404(Origin, pk=pk) 
        data = OriginSerializer(origin).data 
        return Response(data)

