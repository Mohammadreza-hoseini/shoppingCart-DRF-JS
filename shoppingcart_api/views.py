from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer


class ListProducts(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer