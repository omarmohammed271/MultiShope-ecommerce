from . models import CartItem

def count(request,cart_count=0):
    user = request.user
    if user.is_authenticated:
        items = CartItem.objects.filter(user=user)
        cart_count = items.count()
    return {'cart_count':cart_count,}    