from django.contrib import admin

from products.forms import ColorModelForm
from products.models import CategoryModel, ProductTagModel, BrandModel, ProductModel, SizeModel, ColorModel, \
    ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

    search_fields = ['title']
    list_display = ['title', 'created_at']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['code']
    search_fields = ['code']
    form = ColorModelForm

class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['tags', 'category', 'brand', 'sizes', 'colors']
    readonly_fields = ['real_price']
    inlines = [ProductImageStackedInline]