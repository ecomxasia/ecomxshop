from django.contrib import admin

# Register your models here.
from .models import Product, UCategory, MCategory, LCategory, ProductCode, RelativeProduct

class MCategoryInline(admin.StackedInline):
    model = MCategory
    extra = 0

class UCategoryAdmin(admin.ModelAdmin):
    inlines = [ MCategoryInline ]
    list_display = ( 'category_name', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'category_name' ]

class LCategoryInline(admin.StackedInline):
    model = LCategory
    extra = 0

class MCategoryAdmin(admin.ModelAdmin):
    inlines = [ LCategoryInline ]
    list_display = ( 'category_name', 'upper_category', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'category_name' ]

class LCategoryAdmin(admin.ModelAdmin):
    list_display = ( 'category_name', 'upper_category', 'create_date' )
    list_filter = [ 'create_date' ]
    search_fields = [ 'category_name' ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'brand', 'origin', 'size', 'color', 'sale_price', 'purchase_price', 'create_date')
    list_filter = [ 'create_date', 'update_date' ]
    #search_fields = ['product_name', 'brand', 'origin', 'manufacture_short_name', 'size', 'color']
    fieldsets = [
        (None, { 'fields': ['product_name', 'product_short_name', 'category', 'store'] }),
        ('기준 정보', { 'fields': ['brand','origin','manufacture'] } ),
        ('속성 정보', { 'fields': ['size','color','box_type'] } ),
        ('가격/원가', { 'fields': ['sale_price','purchase_price','tax_class'] } ),
        ('주문 규칙', { 'fields': ['available_quantity','min_order_quantity','out_of_stock_status'] } ),
        ('META', { 'fields': ['meta_tag','meta_keyword','product_tags'] } ),
        ('상세 설명', { 'fields': ['description'] } ),
    ]

class RelativeProductAdmin(admin.ModelAdmin):
    list_display = ('area', 'product', 'relative_product', 'update_date')

class ProductCodeAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_code_type', 'code_value', 'update_date')

admin.site.register(UCategory, UCategoryAdmin)
admin.site.register(MCategory, MCategoryAdmin)
admin.site.register(LCategory, LCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCode, ProductCodeAdmin)
admin.site.register(RelativeProduct, RelativeProductAdmin)