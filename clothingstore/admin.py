from django.contrib import admin
from .models import Category, Product, ProductImage, Stock, Subcategory

admin.site.register(Category)


class ColorInline(admin.TabularInline):
    model = Product.colors.through


class ProductAdmin(admin.ModelAdmin):
    inlines = [ColorInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)
    search_fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_filter = ('parent_category',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Stock)
