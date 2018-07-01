from rest_framework import serializers
from .models import Brand, Origin

class BrandSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Brand
        fields = ('brand_name','brand_short_name')
        
class OriginSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Origin
        fields = ('origin_name','origin_short_name')
        