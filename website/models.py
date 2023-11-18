from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="subcategory")

    def __str__(self):
        return self.name
    
    def get_subppage_url(self):
        return reverse("subpage", kwargs={'id':self.id})
    
class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField()
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return self.name
    
    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'id':self.id})
    
class OrderItem(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE, related_name="order_item")
    quantity = models.IntegerField(default=1)

    def get_delete_cart_item_url(self):
        return reverse("delete_cart_item", kwargs={'id':self.id})

    #def __str__(self):
        #return self.product + ": " + self.quantity






    
