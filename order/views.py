from django.shortcuts import render
from .models import OrderProduct,Order
from cart.models import CartItem
# Create your views here.


def place_order(request,total=0,shipping=0,discount=0,grand_total=0):
    user= request.user
    items = CartItem.objects.filter(user=user)


    context ={
        'items':items,
        'total':total,
        'shipping':shipping,
        'discount':discount,
        'grand_total':grand_total,
    }

    return render(request,'order/order.html',context)