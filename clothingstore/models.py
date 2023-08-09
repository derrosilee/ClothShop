from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20)


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to='product_images/')
    image_2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_6 = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.product


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField()
