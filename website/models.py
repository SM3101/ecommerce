from django.db import models

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
    
class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField()
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return self.name




    
