from django.contrib import admin
from .models import Order,OrderProduct
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass

