import datetime
from django.db import models
from django.utils import timezone
from commoncode.models import Origin, Brand, Manufacture, Store

# Create your models here.

class UCategory(models.Model):
    category_name = models.CharField(max_length=10)
    register_date = models.DateTimeField('date registered', auto_now=True)
    def __str__(self):
        return self.category_name

class MCategory(models.Model):
    category_name = models.CharField(max_length=10)
    upper_category = models.ForeignKey(UCategory, on_delete=models.CASCADE)
    register_date = models.DateTimeField('date registered', auto_now=True)
    def __str__(self):
        return self.category_name

class LCategory(models.Model):
    category_name = models.CharField(max_length=10)
    upper_category = models.ForeignKey(MCategory, on_delete=models.CASCADE)
    register_date = models.DateTimeField('date registered', auto_now=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    SIZE = (
        ( 'S', 'Small' ),
        ( 'M', 'Midium' ),
        ( 'L', 'Large' ),
        ( 'X', 'N/A' ),
    )
    COLOR = (
        ( 'BLUE', 'Blue' ),
        ( 'WHITE', 'White' ),
        ( 'BLACK', 'Black' ),
        ( 'GREY', 'Grey' ),
        ( 'NA', 'N/A' ),
    )
    product_name = models.CharField(max_length=200)
    product_short_name = models.CharField(max_length=50)
    category = models.CharField(max_length=3) ##
    related_product = models.CharField(max_length=3, null=True) ##
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    register_date = models.DateTimeField('date registered', auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZE) ##
    color = models.CharField(max_length=10, choices=COLOR) ##
    sale_price = models.FloatField('Sale Price')
    purchase_price = models.FloatField('Purchase Price')
    description = models.TextField(max_length=1000)
    meta_tag = models.CharField(max_length=300, null=True)
    meta_keyword = models.CharField(max_length=300, null=True)
    product_tags = models.CharField(max_length=300, null=True)
    local_barcode = models.CharField(max_length=30, null=True)
    model = models.CharField(max_length=30, null=True)
    sku = models.CharField(max_length=30, null=True)
    upc = models.CharField(max_length=30, null=True)
    ean = models.CharField(max_length=30, null=True)
    jan = models.CharField(max_length=30, null=True)
    isbn = models.CharField(max_length=30, null=True)
    mpn = models.CharField(max_length=30, null=True)
    tax_class = models.CharField(max_length=3) ##
    quantity = models.IntegerField(default=999)
    min_quantity = models.IntegerField(default=1)
    out_of_stock_status = models.CharField(max_length=3) ##
    box_type = models.CharField(max_length=3) ##

    def __str__(self):
        return self.product_name

    def was_registered_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.register_date <= now