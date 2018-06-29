from django.urls import path
from .views import Product, Brand, Origin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", products_list, name="products_list"), 
    path("products/<int:pk>/", products_detail, name="products_detail"),
    path("brands/", brands_list, name="brands_list"),
    path("brands/<int:pk>/", brands_detail, name="brands_detail"),
    path("origins/", origins_list, name="origins_list"),
    path("origins/<int:pk>/", origins_detail, name="origins_detail"),
]