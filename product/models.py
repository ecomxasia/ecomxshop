import datetime
from django.db import models
from django.utils import timezone
from commoncode.models import Origin, Brand, Manufacture, Store, CommonCode

# Create your models here.

def get_SIZE():
    return CommonCode.objects.filter(code_group='SIZE')

class UCategory(models.Model):
    category_name = models.CharField(max_length=10)
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    def __str__(self):
        return self.category_name

class MCategory(models.Model):
    category_name = models.CharField(max_length=10)
    upper_category = models.ForeignKey(UCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    def __str__(self):
        return self.category_name

class LCategory(models.Model):
    category_name = models.CharField(max_length=10)
    upper_category = models.ForeignKey(MCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_short_name = models.CharField(max_length=50)
    category = models.CharField(max_length=3) ##
    related_product = models.CharField(max_length=3, blank=True) ##
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    update_date = models.DateTimeField('Date Updated', auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    size = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'SIZE'}, related_name="product.size+",) 
    color = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'COLOR'}, related_name="product.color+",) 
    sale_price = models.FloatField('Sale Price')
    purchase_price = models.FloatField('Purchase Price')
    description = models.TextField(max_length=1000)
    meta_tag = models.CharField(max_length=300, blank=True)
    meta_keyword = models.CharField(max_length=300, blank=True)
    product_tags = models.CharField(max_length=300, blank=True)
    model = models.CharField(max_length=30, blank=True)
    tax_class = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'TAXMETHOD'}, related_name="tax class+",) 
    available_quantity = models.IntegerField(default=999)
    min_order_quantity = models.IntegerField(default=1)
    out_of_stock_status = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'ORDSTOCK'}, related_name="out of stock status+",) 
    box_type = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'SHPBOX'}, related_name="box type+",) 
    status = models.ForeignKey(CommonCode, on_delete=models.CASCADE, limit_choices_to={'code_group': 'PRDSTATUS'}, related_name="status", )

    def __str__(self):
        return self.product_name

    def was_registered_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.register_date <= now

class RelativeProduct(models.Model):
    area = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    relative_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="relative_product")
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    update_date = models.DateTimeField('Date Updated', auto_now=True)

class ProductCode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_code_type = models.CharField(max_length=4)
    code_value = models.CharField(max_length=64)
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    update_date = models.DateTimeField('Date Updated', auto_now=True)
