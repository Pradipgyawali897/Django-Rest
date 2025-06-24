from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product

class MyProductSerilizer(ModelSerializer):
    tax=serializers.Serializer(read_only=True)
    class Meta:
        
        def get_tax(self,obj):
            return 12.3
        model=Product
        fields=[
            'id','title','content','price','tax',
        ]
