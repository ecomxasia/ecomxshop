from django.db import models

# Create your models here.

class CommonCode(models.Model):
    code_group = models.CharField(max_length=10) ##
    code_group_name = models.CharField(max_length=30) ##
    code_type  = models.CharField(max_length=10) ##
    code_type_name  = models.CharField(max_length=30) ##
    code_key   = models.CharField(max_length=20) ##
    code_value = models.CharField(max_length=100) ##
    description = models.TextField() ##
    create_date = models.DateTimeField('Date Created', auto_now_add=True)
    update_date = models.DateTimeField('Date Update', auto_now=True)
    seq = models.IntegerField(blank=True)
    cond = models.CharField(max_length=10, blank=True)
 
    def __str__(self):
        return self.code_value

class Origin(models.Model):
    origin_name = models.CharField(max_length=100)
    origin_short_name = models.CharField(max_length=50)
    create_date = models.DateTimeField('date created', auto_now=True)
    def __str__(self):
        return self.origin_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_short_name = models.CharField(max_length=50)
    create_date = models.DateTimeField('date created', auto_now=True)
    def __str__(self):
        return self.brand_name

class Manufacture(models.Model):
    manufacture_name = models.CharField(max_length=100)
    manufacture_short_name = models.CharField(max_length=50)
    create_date = models.DateTimeField('date created', auto_now=True)
    def __str__(self):
        return self.manufacture_name

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created', auto_now=True)
    def __str__(self):
        return self.store_name
    
    