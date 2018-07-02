from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    list_display = (
        'product', 
        'product_brand', 
        'product_origin', 
        'product_size', 
        'product_color', 
        'user', 'order_date', 'payment_method', 'payment_amount', 'order_status')
    list_filter = [ 'order_date', 'payment_method', 'order_status', 'shipping_method', 'shipping_status' ]
    #search_fields = ['product_size', 'product_brand' ]
    #date_hierarchy = 'order_date'

admin.site.register(Order, OrderAdmin)