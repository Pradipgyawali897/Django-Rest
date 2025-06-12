from rest_framework import generics

from product.models import Product
from product.serilizer import MyProductSerilizer

# class ProductDetailView(generics.RetrieveAPIView):
#     queryset=Product.objects.all()
#     serializer_class=MyProductSerilizer
#     lookup_field='pk'
    

class ListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=MyProductSerilizer
    def perform_create(self, serializer):
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=serializer.validated_data.get('title')
        serializer.save(content=content)         


class RetriveDestroyUpdateApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=MyProductSerilizer
    lookup_field='pk'
# class ProductListView(generics.ListAPIView):
#     queryset=Product.objects.all()
#     serializer_class=MyProductSerilizer
