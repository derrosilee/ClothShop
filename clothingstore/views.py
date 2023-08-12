from django.shortcuts import render
from .models import ProductImage, Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'clothingstore/product_list.html', {'products': products})
