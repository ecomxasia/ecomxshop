from django.db import models

# Create your models here.

class CommonCode(models.Model):
    code_group = models.CharField(verbose_name='코드그룹', max_length=10) ##
    code_group_name = models.CharField(verbose_name='코드그룹명', max_length=30) ##
    code_type  = models.CharField(verbose_name='코드타입', max_length=10) ##
    code_type_name  = models.CharField(verbose_name='코드타입명', max_length=30) ##
    code_key   = models.CharField(verbose_name='코드', max_length=20) ##
    code_value = models.CharField(verbose_name='코드값', max_length=100) ##
    description = models.TextField(verbose_name='설명', ) ##
    create_date = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='변경일시', auto_now=True)
    seq = models.IntegerField(verbose_name='순번', blank=True)
    cond = models.CharField(verbose_name='필터조건', max_length=10, blank=True)
 
    def __str__(self):
        return self.code_value

class Origin(models.Model):
    origin_name = models.CharField(verbose_name='원산지', max_length=100)
    origin_short_name = models.CharField(verbose_name='원산지s', max_length=50)
    create_date = models.DateTimeField(verbose_name='생성일시', auto_now=True)
    def __str__(self):
        return self.origin_name

class Brand(models.Model):
    brand_name = models.CharField(verbose_name='브랜드', max_length=100)
    brand_short_name = models.CharField(verbose_name='브랜드s', max_length=50)
    create_date = models.DateTimeField(verbose_name='생성일시',  auto_now=True)
    def __str__(self):
        return self.brand_name

class Manufacture(models.Model):
    manufacture_name = models.CharField(verbose_name='제조사', max_length=100)
    manufacture_short_name = models.CharField(verbose_name='제조사s', max_length=50)
    create_date = models.DateTimeField(verbose_name='생성일시', auto_now=True)
    def __str__(self):
        return self.manufacture_name

class Store(models.Model):
    store_name = models.CharField(verbose_name='매장명', max_length=100)
    location = models.CharField(verbose_name='위치', max_length=100)
    manager = models.CharField(verbose_name='관리자', max_length=100)
    create_date = models.DateTimeField(verbose_name='생성일시', auto_now=True)
    def __str__(self):
        return self.store_name
    
    