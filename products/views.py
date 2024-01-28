from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Product,BestSeller,Accept_Product
from .serializers import CategorySerializer,ProductSerializer,BestSellerSerilizer,AcceptProductSerializer
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class BestSellerView(viewsets.ModelViewSet):
    queryset=BestSeller.objects.all()
    serializer_class=BestSellerSerilizer


class AcceptProductView(viewsets.ModelViewSet):
    queryset=Accept_Product.objects.all()
    serializer_class=AcceptProductSerializer



