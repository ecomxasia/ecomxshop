import datetime
from django.db import models
from django.utils import timezone
from product.models import Product
from commoncode.models import Store, CommonCode
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="size",) 
    color = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="color",) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_date = models.DateTimeField('Date Ordered', auto_now=True)
    payment_method = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="payment method+",)
    payment_amount = models.FloatField('Payment Amount')
    payment_date = models.DateTimeField('Date Paid', auto_now=True)
    order_status = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="order status+",)
    shipping_method = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="shipping method+",)
    shipping_zip = models.CharField(max_length=10)
    shipping_address = models.CharField(max_length=200)
    shipping_name = models.CharField(max_length=100)
    shipping_status = models.ForeignKey(CommonCode, on_delete=models.CASCADE, related_name="shipping status+",)

    def __str__(self):
        return self.origin_name
    
    def was_ordered_recently(self):
        now = timezone.now()
        return now <= self.ordered_date < now - datetime.timedelta(days=3)