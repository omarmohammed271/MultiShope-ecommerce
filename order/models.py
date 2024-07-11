from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address1 = models.CharField( max_length=250)
    address2 = models.CharField( max_length=250,blank=True,null=True)
    city = models.CharField( max_length=250)

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'
    
    def __str__(self) -> str:
        return f'{self.user}'
    

class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_details = models.TextField()
    total = models.FloatField()
    discount = models.FloatField(blank=True,null=True)
    shipping = models.FloatField()
    grand_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.user)
    
   
