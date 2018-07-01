from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from .models import Brand, Origin, Manufacture
from .serializers import BrandSerializer, OriginSerializer

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
