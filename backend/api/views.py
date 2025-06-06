from django.shortcuts import render
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serilizer import MyProductSerilizer

@api_view(['GET'])
def api_home(request,*args, **kwargs):
      data={ }
      serilizer=MyProductSerilizer(data=request.data)
      if serilizer.is_valid():
              instance=serilizer.save()
              print(instance)
              data=serilizer.data
      return Response(data)
    
