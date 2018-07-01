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
from product.apiviews import ProductList, ProductDetail
from commoncode.apiviews import BrandList, BrandDetail, OriginList, OriginDetail
from product.apiviews import LoginView, UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path("products/", ProductList.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="products_detail"),
    path("brands/", BrandList.as_view(), name="brands_list"),
    path("brands/<int:pk>/", BrandDetail.as_view(), name="brands_detail"),
    path("origins/", OriginList.as_view(), name="origins_list"),
    path("origins/<int:pk>/", OriginDetail.as_view(), name="origins_detail"),
    path("users/", UserCreate.as_view(), name="user_create"),
] 
