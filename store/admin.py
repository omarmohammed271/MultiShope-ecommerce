from django.contrib import admin
from .models import Category,Size,Color,Product,ImageProducts
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name','slug'


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageProducts)
class ImageProductsAdmin(admin.ModelAdmin):
    pass


