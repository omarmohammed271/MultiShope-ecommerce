from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=150)    

    def __str__(self) -> str:
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=150)    

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    price = models.FloatField()
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("store:product_detail",args=[self.category.slug,self.slug])
    

def image_upload(instance,file_name:str):
    extenstion = file_name.split('.')[1]
    return f'products/{instance.product.name}.{extenstion}'   

class ImageProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return f'Images of {self.product}'
    