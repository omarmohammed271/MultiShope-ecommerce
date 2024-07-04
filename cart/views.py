from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .models import CartItem
from store.models import Product
# Create your views here.
## Add Product to cart
@login_required(login_url='accounts:login')
def add_cart(request,slug=None):
    user = request.user
    product = get_object_or_404(Product,slug=slug)
    if request.method=='POST':
        size = request.POST.get('size')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')

        item = CartItem.objects.filter(user=user,product=product,color=color,size=size).exists()
        ## Create
        if not item:
            item = CartItem.objects.create(
                user=user,product=product,size=size,color=color,
                quantity=quantity
            )
            return redirect('cart:cart')

        ## Update
        item = CartItem.objects.get(user=user,product=product,size=size,color=color)
        item.quantity = quantity
        item.save()
        return redirect('cart:cart')

def remove(request,product_id,item_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    item = CartItem.objects.get(user=user,product=product,id=item_id)
    item.delete()
    return redirect('cart:cart')

@login_required(login_url='accounts:login')
def cart(request):
    user = request.user
    items = CartItem.objects.filter(user=user)
    total = [item.total for item in items][0]
    shipping = total * 0.10
    grand_total = shipping + total

    context = {
        'items':items,
        'total':total,
        'shipping':shipping,
        'grand_total':grand_total,
    }
    return render(request,'cart/cart.html',context)