from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,ImageProducts,Size,Color,Category
from django.core.paginator import Paginator
# Create your views here.

def store(request):
    products = Product.objects.prefetch_related('images').all()
    paginator = Paginator(products, 2)  

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'products':page_obj,
    }
    return render(request,'store/store.html',context)

def product_detail(request,category_slug,slug):
    product = get_object_or_404(Product,category__slug=category_slug,slug=slug)
    return render(request,'store/product_detail.html')