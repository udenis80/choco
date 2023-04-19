from django.shortcuts import render
from django.views import View

from .models import Product

def index(request):
    return render(request, 'products/index.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'products/shop.html', {'pr': products})


def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def product_detail(request):
    return render(request, 'products/product-details.html')