from django.contrib import admin

# Register your models here.
from .models import Origin, Brand, Manufacture, Store, CommonCode

class OriginAdmin(admin.ModelAdmin):
    list_display = ( 'origin_name', 'origin_short_name', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'origin_name' ]

class BrandAdmin(admin.ModelAdmin):
    list_display = ( 'brand_name', 'brand_short_name', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'brand_name' ]

class ManufactureAdmin(admin.ModelAdmin): 
    list_display = ( 'manufacture_name', 'manufacture_short_name', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'manufacture_name' ]

class StoreAdmin(admin.ModelAdmin):
    list_display = ( 'store_name', 'location', 'manager', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'store_name', 'location', 'manager' ]

class CommonCodeAdmin(admin.ModelAdmin):
    list_display = ( 'code_group', 'code_group_name', 'code_type', 'code_type_name', 'code_key', 'code_value', 'description', 'create_date' )
    list_filter = [ 'code_group_name', 'code_type_name', 'create_date' ]
    search_fields = [ 'code_group', 'code_group_name', 'code_type', 'code_type_name', 'code_key', 'code_value', 'description' ]

admin.site.register(Store, StoreAdmin)
admin.site.register(Origin, OriginAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(CommonCode, CommonCodeAdmin)