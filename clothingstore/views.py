from django.shortcuts import render
from .models import ProductImage, Product


def product_list(request):
    products = Product.objects.all()
    product_images = ProductImage.objects.all()
    context = {
        'products': products,
        'product_images': product_images
    }
    return render(request, 'clothingstore/product_list.html', context)
