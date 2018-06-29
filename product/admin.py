from django.contrib import admin

# Register your models here.
from .models import Origin, Brand, Manufacture, Store, Product, UCategory, MCategory, LCategory

class OriginAdmin(admin.ModelAdmin):
    list_display = ( 'origin_name', 'origin_short_name', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'origin_name' ]

class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'brand_name', 'brand_short_name', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'brand_name' ]

class ManufactureAdmin(admin.ModelAdmin): 
    list_display = ( 'manufacture_name', 'manufacture_short_name', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'manufacture_name' ]

class StoreAdmin(admin.ModelAdmin):
    list_display = ( 'store_name', 'location', 'manager', 'register_date' )
    list_filter = [ 'register_date' ]
    search_fields = [ 'store_name', 'location', 'manager' ]

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


admin.site.register(Origin, OriginAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(UCategory, UCategoryAdmin)
admin.site.register(MCategory, MCategoryAdmin)
admin.site.register(LCategory, LCategoryAdmin)
admin.site.register(Product, ProductAdmin)