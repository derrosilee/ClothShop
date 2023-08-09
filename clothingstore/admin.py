from django.contrib import admin
from .models import Category, Product, ProductImage, Stock

admin.site.register(Category)


class ColorInline(admin.TabularInline):
    model = Product.colors.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Stock)
