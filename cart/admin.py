from django.contrib import admin
from .models import CartItem,Coupon
# Register your models here.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = 'user','product','size','color','quantity','sub_total','total'
    list_filter = 'user',

admin.site.register(Coupon)