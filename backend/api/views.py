from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from product.models import Product
from 
def api_home(request,*args, **kwargs):
    model_data=Product.objects.order_by('?').first()
    data={ }
    if model_data:
       data=model_to_dict(model_data)
    return JsonResponse(data)
    
