from django.shortcuts import render
from django.views import View

from .models import Product



class ProductsView(View):
    """Виды продукции"""
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products/index.html', {'index': products})