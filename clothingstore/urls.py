from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('products-list/', views.product_list, name="product-list")
]
