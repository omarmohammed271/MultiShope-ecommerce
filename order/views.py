from django.shortcuts import render,redirect
from .models import OrderProduct,Order
from cart.models import CartItem
from store.models import Product
# Create your views here.


def place_order(request,total=0,shipping=0,discount=0,grand_total=0):
    user= request.user
    order_details = ''
    items = CartItem.objects.filter(user=user)
    print(items)
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        order = Order.objects.create(
            user=user,f_name=f_name,l_name=l_name,
            email=email,phone=phone,
            address1=address1,address2=address2,
            city=city,
        )
        for item in items:
            order_details += f'Product:{item.product} price:{item.product.price} Quantity:{item.quantity} Size:{item.size} Color:{item.color}\n'
            product = Product.objects.get(id=item.product.id)
            product.stock -= item.quantity
            product.save()

        order_product = OrderProduct.objects.create(
            user=user,order=order,order_details=order_details,
            total=total,discount=discount,shipping=shipping,
            grand_total=grand_total
        )  
        CartItem.objects.filter(user=user).delete()  
        return redirect('home')





    context ={
        'items':items,
        'total':total,
        'shipping':shipping,
        'discount':discount,
        'grand_total':grand_total,
    }

    return render(request,'order/order.html',context)