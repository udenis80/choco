from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from chocolate.models import Product

def index(request):
    return render(request, 'index.html')
def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'shop.html', context)

def product_detail(request):
    return render(request, 'product_detail.html')
