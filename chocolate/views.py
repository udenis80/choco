from django.shortcuts import render
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

# class ProductDetailView(DetailView):
#     """Полное описание товара"""
#     model = Product
#     # queryset = Product.objects.filter(draft=False)
#     slug_field = "url"
