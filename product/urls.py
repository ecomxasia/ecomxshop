from django.urls import path
from .views import Product, Brand, Origin

urlpatterns = [
    path('admin/', admin.site.urls),

]