from django.shortcuts import render
from django.views import View

from .models import Product

def index(request):
    return render(request, 'index.html')



# def shop(request):
#     products = Product.objects.all()
#     return render(request, 'products/shop.html', {'pr': products})
