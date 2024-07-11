from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.user} Product: {self.product}'
    
    
    @property
    def sub_total(self):
        return self.product.price * self.quantity
    
    @property
    def total(self):
        total = 0
        items = CartItem.objects.filter(user=self.user)##Advanced
        for item in items:
            total += item.sub_total
        return total    
    
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField()
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.code