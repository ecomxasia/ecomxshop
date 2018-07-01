from django.contrib import admin

# Register your models here.
from .models import Product, UCategory, MCategory, LCategory

class MCategoryInline(admin.StackedInline):
    model = MCategory
    extra = 0

class UCategoryAdmin(admin.ModelAdmin):
    inlines = [ MCategoryInline ]
    list_display = ( 'category_name', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'category_name' ]

class LCategoryInline(admin.StackedInline):
    model = LCategory
    extra = 0

class MCategoryAdmin(admin.ModelAdmin):
    inlines = [ LCategoryInline ]
    list_display = ( 'category_name', 'upper_category', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'category_name' ]

class LCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'category_name', 'upper_category', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'category_name' ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand', 'origin', 'size', 'color', 'sale_price', 'purchase_price', 'register_date')
#    list_filter = [ 'register_date', 'brand', 'origin' ]
#    search_fields = ['product_name', 'brand', 'origin', 'manufacture_short_name', 'size', 'color']


admin.site.register(UCategory, UCategoryAdmin)
admin.site.register(MCategory, MCategoryAdmin)
admin.site.register(LCategory, LCategoryAdmin)
admin.site.register(Product, ProductAdmin)