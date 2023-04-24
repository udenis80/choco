from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from chocolate.models import Product


def index(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'index.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def product_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

