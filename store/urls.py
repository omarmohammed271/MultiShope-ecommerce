from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.store,name='store'),
    path('product/<str:category_slug>/<str:slug>/',views.product_detail,name='product_detail'),
]
