from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('place-order/<str:total>/<str:shipping>/<str:discount>/<str:grand_total>/',views.place_order,name='place_order'),
]
