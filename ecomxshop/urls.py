"""ecomxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. thAdd an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.views import products_list, products_detail, brands_detail, brands_list, origins_list, origins_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", products_list, name="products_list"), 
    path("products/<int:pk>/", products_detail, name="products_detail"),
    path("brands/", brands_list, name="brands_list"),
    path("brands/<int:pk>/", brands_detail, name="brands_detail"),
    path("origins/", origins_list, name="origins_list"),
    path("origins/<int:pk>/", origins_detail, name="origins_detail"),
]
