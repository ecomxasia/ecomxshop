from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse
from .models import Product, Brand

def products_list(request):
    MAX_OBJECTS = 20
    products = Product.objects.all()[:20]
    data = {"results": list(products.values("product_name", "brand", "origin", "register_date"))}
    return JsonResponse(data)

def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk) 
    data = {"results": {
        "product_name": product.product_name,
        "product_shot_name": product.product_short_name,
        "category": product.category,
        #"store": product.store,

        #"brand": product.brand,
        "sale_price": product.sale_price,
        "description": product.description,
        "model": product.model,
        "quantity": product.quantity,
        "min_quantity": product.min_quantity,
        "box_type": product.box_type,

        "register_date": product.register_date
    }}
    return JsonResponse(data)

def brands_list(request):
    MAX_OBJECTS = 20
    brands = Brand.objects.all()[:20]
    data = {"results": list(brands.values("brand_name", "register_date"))}
    return JsonResponse(data)

def brands_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk) 
    data = {"results": {
        "product_name": brand.brand_name,
        "register_date": brand.register_date
    }}
    return JsonResponse(data)

def origin_list(request):
    MAX_OBJECTS = 20
    origins = Origin.objects.all()[:20]
    data = {"results": list(origins.values("origin_name", "register_date"))}
    return JsonResponse(data)

def origin_detail(request, pk):
    origin = get_object_or_404(Origin, pk=pk) 
    data = {"results": {
        "origin_name": origin.origin_name,
        "register_date": origin.register_date
    }}
    return JsonResponse(data)