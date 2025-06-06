from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product

class MyProductSerilizer(ModelSerializer):
    tax=serializers.Serializer(read_only=True)
    class Meta:
        model=Product
        fields=[
            'title','content','tax','price',
        ]
    
    def get_tax(self,obj):
        return "13%"
    