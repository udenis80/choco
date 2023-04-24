from django.shortcuts import render
from chocolate.models import Product


def index(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'index.html', context)
