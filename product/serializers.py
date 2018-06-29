from rest_framework import serializers
from .models import Product, Brand, Origin
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = { 'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BrandSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Brand
        fields = ('brand_name','brand_short_name')
        
class OriginSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Origin
        fields = ('origin_name','origin_short_name')
        
class ProductSerializer(serializers.ModelSerializer): 
    brand = BrandSerializer(many=False, read_only=True, required=False)
    origin = OriginSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = Product
        fields = '__all__'

